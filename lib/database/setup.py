
from database import conn,cursor

def create_tables():

    cursor.execute('''CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT,
                   email TEXT
                   )
                   ''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS categories(
                   category_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   category_name TEXT
                   )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses(
                    expense_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    amount INTEGER NOT NULL,
                    description TEXT,
                    user_id INTEGER,
                    category_id INTEGER,
                    FOREIGN KEY (user_id) REFERENCES Users(user_id),
                    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
                   )''')
    
    conn.commit()
    conn.close()


    