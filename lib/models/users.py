import sqlite3

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    def __str__(self):
        return f"User(username='{self.username}', email='{self.email}')"

    @staticmethod
    def create_user(username, email):
        conn = sqlite3.connect('expense.db')
        c = conn.cursor()
        try:
            c.execute('INSERT INTO users (username, email) VALUES (?, ?)', (username, email))
            conn.commit()
            print(f"User '{username}' created successfully.")
        except sqlite3.IntegrityError:
            print(f"User '{username}' already exists.")
        finally:
            conn.close()

    @staticmethod
    def get_user_by_id(user_id):
        conn = sqlite3.connect('expense.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        user_data = c.fetchone()
        conn.close()
        if user_data:
            return User(username=user_data[1], email=user_data[2])
        else:
            return None

    @staticmethod
    def get_all_users():
        conn = sqlite3.connect('expense.db')
        c = conn.cursor()
        c.execute('SELECT * FROM users')
        users_data = c.fetchall()
        conn.close()
        users = []
        for user_data in users_data:
            users.append(User(username=user_data[1], email=user_data[2]))
        return users

    @staticmethod
    def delete_user(user_id):
        conn = sqlite3.connect('expense.db')
        c = conn.cursor()
        c.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()
        if c.rowcount > 0:
            print(f"User with ID {user_id} deleted successfully.")
        else:
            print(f"User with ID {user_id} not found.")

        conn.close()

      