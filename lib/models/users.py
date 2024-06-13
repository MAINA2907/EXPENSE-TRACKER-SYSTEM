import sqlite3

class User:

    all = {}

    def __init__(self, username, email, id=None):
        self.username = username
        self.email = email
        self.id = id
    
    def __str__(self):
        return f"User(username='{self.username}', email='{self.email}')"
    


    @classmethod
    def add_user(cls, username, email):
        user = cls(username=username, email=email)
        user.save()
        return user

    def save(self):
        conn = sqlite3.connect('expense.db')
        c = conn.cursor()
        try:
            if self.id is None:
                c.execute('INSERT INTO users (username, email) VALUES (?, ?)', (self.username, self.email))
                self.id = c.lastrowid
                type(self).all[self.id] = self
                print(f"User '{self.username}' created successfully.")
            else:
                c.execute('UPDATE users SET username = ?, email = ? WHERE id = ?', (self.username, self.email, self.id))
                print(f"User with ID {self.id} updated successfully.")
            conn.commit()
        except sqlite3.IntegrityError:
            print(f"User '{self.username}' already exists.")
        finally:
            conn.close()

    def delete(self):
        if self.id is None:
            print("Cannot delete an unsaved user.")
            return
        
        conn = sqlite3.connect('expense.db')
        c = conn.cursor()
        c.execute('DELETE FROM users WHERE id = ?', (self.id,))
        conn.commit()
        if c.rowcount > 0:
            print(f"User with ID {self.id} deleted successfully.")
            self.id = None
        else:
            print(f"User with ID {self.id} not found.")
        conn.close()

    @classmethod
    def get_user_by_id(cls, user_id):
        conn = sqlite3.connect('expense.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        user_data = c.fetchone()
        conn.close()
        if user_data:
            return cls(username=user_data[1], email=user_data[2], id=user_data[0])
        else:
            return None

    @classmethod
    def get_all_users(cls):
        conn = sqlite3.connect('expense.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users')
        users_data = c.fetchall()
        conn.close()
        users = []
        for user_data in users_data:
            users.append(cls(username=user_data[1], email=user_data[2], id=user_data[0]))
        return users
