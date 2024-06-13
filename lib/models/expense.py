import sqlite3

class Expense:
    all = {}

    def __init__(self, amount, description, user_id, category_id, id=None):
        self.amount = amount
        self.description = description
        self.user_id = user_id
        self.category_id = category_id
        self.id = id
    
    def __str__(self):
        return f"Expense(amount={self.amount}, description='{self.description}', user_id={self.user_id}, category_id={self.category_id})"
    
    @classmethod
    def create_expense(cls, amount, description, user_id, category_id):
        expense = cls(amount=amount, description=description, user_id=user_id, category_id=category_id)
        expense.save()
        return expense
    
    def save(self):
        conn = sqlite3.connect('expense.db')
        c = conn.cursor()
        try:
            if self.id is None:
                c.execute('INSERT INTO expenses (amount, description, user_id, category_id) VALUES (?, ?, ?, ?)', 
                          (self.amount, self.description, self.user_id, self.category_id))
                self.id = c.lastrowid
                type(self).all[self.id] = self
                print("Expense created successfully.")
            else:
                c.execute('UPDATE expenses SET amount = ?, description = ?, user_id = ?, category_id = ? WHERE expense_id = ?', 
                          (self.amount, self.description, self.user_id, self.category_id, self.id))
                print("Expense updated successfully.")
            conn.commit()
        except sqlite3.IntegrityError:
            print("Failed to save expense.")
        finally:
            conn.close()
    
    def delete(self):
        if self.id is None:
            print("Cannot delete an unsaved expense.")
            return
        
        conn = sqlite3.connect('expense.db')
        c = conn.cursor()
        c.execute('DELETE FROM expenses WHERE expense_id = ?', (self.id,))
        conn.commit()
        if c.rowcount > 0:
            print(f"Expense with ID {self.id} deleted successfully.")
            self.id = None
        else:
            print(f"Expense with ID {self.id} not found.")
        conn.close()

    @classmethod
    def get_expense_by_id(cls, expense_id):
        conn = sqlite3.connect('expense.db')
        c = conn.cursor()
        c.execute('SELECT * FROM expenses WHERE expense_id = ?', (expense_id,))
        expense_data = c.fetchone()
        conn.close()
        if expense_data:
            return cls(amount=expense_data[1], description=expense_data[2], user_id=expense_data[3], category_id=expense_data[4], id=expense_data[0])
        else:
            return None

    @classmethod
    def get_all_expenses(cls):
        conn = sqlite3.connect('expense.db')
        c = conn.cursor()
        c.execute('SELECT * FROM expenses')
        expenses_data = c.fetchall()
        conn.close()
        expenses = []
        for expense_data in expenses_data:
            expenses.append(cls(amount=expense_data[1], description=expense_data[2], user_id=expense_data[3], category_id=expense_data[4], id=expense_data[0]))
        return expenses
