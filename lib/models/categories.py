import sqlite3

class Category:
    def __init__(self, category_name):
        self.category_name = category_name
    
    def __str__(self):
        return f"Category(category_name='{self.category_name}')"

    @staticmethod
    def create_category(category_name):
        conn = sqlite3.connect('expense.db')
        c = conn.cursor()
        try:
            c.execute('INSERT INTO categories (category_name) VALUES (?)', (category_name,))
            conn.commit()
            print(f"Category '{category_name}' created successfully.")
        except sqlite3.IntegrityError:
            print(f"Category '{category_name}' already exists.")
        finally:
            conn.close()

    @staticmethod
    def get_category_by_id(category_id):
        conn = sqlite3.connect('expense.db')
        c = conn.cursor()
        c.execute('SELECT * FROM categories WHERE category_id = ?', (category_id,))
        category_data = c.fetchone()
        conn.close()
        if category_data:
            return Category(category_name=category_data[1])
        else:
            return None

    @staticmethod
    def get_all_categories():
        conn = sqlite3.connect('expense.db')
        c = conn.cursor()
        c.execute('SELECT * FROM categories')
        categories_data = c.fetchall()
        conn.close()
        categories = []
        for category_data in categories_data:
            categories.append(Category(category_name=category_data[1]))
        return categories

    @staticmethod
    def delete_category(category_id):
        conn = sqlite3.connect('expense.db')
        c = conn.cursor()
        c.execute('DELETE FROM categories WHERE category_id = ?', (category_id,))
        conn.commit()
        if c.rowcount > 0:
            print(f"Category with ID {category_id} deleted successfully.")
        else:
            print(f"Category with ID {category_id} not found.")
        conn.close()
