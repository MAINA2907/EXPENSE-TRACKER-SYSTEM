import sqlite3

class Category:

    all = {}

    def __init__(self, category_name, id=None):
        self.category_name = category_name
        self.id = id
    
    def __str__(self):
        return f"Category(category_name='{self.category_name}')"
    
    @classmethod
    def add_category(cls, category_name):
        category = cls(category_name = category_name)
        category.save()
        return category

    
    def save(self):
        conn = sqlite3.connect('expense.db')
        c = conn.cursor()
        try:
            if self.id is None:
                c.execute('INSERT INTO categories (category_name) VALUES (?)', (self.category_name,))
                self.id = c.lastrowid
                type(self).all[self.id] = self
                print(f"Category '{self.category_name}' created successfully.")
            else:
                c.execute('UPDATE categories SET category_name = ? WHERE category_id = ?', (self.category_name, self.id))
                print(f"Category with ID {self.id} updated successfully.")
            conn.commit()
        except sqlite3.IntegrityError:
            print(f"Category '{self.category_name}' already exists.")
        finally:
            conn.close()

    def delete(self):
        if self.id is None:
            print("Cannot delete an unsaved category.")
            return
        
        conn = sqlite3.connect('expense.db')
        c = conn.cursor()
        c.execute('DELETE FROM categories WHERE category_id = ?', (self.id,))
        conn.commit()
        if c.rowcount > 0:
            print(f"Category with ID {self.id} deleted successfully.")
            self.id = None
        else:
            print(f"Category with ID {self.id} not found.")
        conn.close()

    @classmethod
    def get_category_by_id(cls, category_id):
        conn = sqlite3.connect('expense.db')
        
        c = conn.cursor()
        c.execute('SELECT * FROM categories WHERE category_id = ?', (category_id,))
        category_data = c.fetchone()
        conn.close()
        if category_data:
            return cls(category_name=category_data[1], id=category_data[0])
        else:
            return None

    @classmethod
    def get_all_categories(cls):
        conn = sqlite3.connect('expense.db')
        c = conn.cursor()
        c.execute('SELECT * FROM categories')
        categories_data = c.fetchall()
        conn.close()
        categories = []
        for category_data in categories_data:
            categories.append(cls(category_name=category_data[1], id=category_data[0]))
        return categories
