import sqlite3

conn = sqlite3.connect('expense.db')
cursor = conn.cursor()