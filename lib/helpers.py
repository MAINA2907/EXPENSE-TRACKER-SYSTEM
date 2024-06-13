# lib/helpers.py
import sqlite3
from models.categories import Category
from models.expense import Expense
from models.users import User

def helper_1():
    print("Performing useful function#1.")


def add_category():
    category_name = input("Enter category name: ")
    try:
        Category.create_category(category_name)
    except Exception as e:
        print(f"Error occurred: {e}")
    input("\nPress Enter to continue...")

def update_category():
    category_id = int(input("Enter category id: "))
    category = Category.get_category_by_id(category_id)
    if category:
        new_name = input("Enter new category name: ")
        try:
            category.update_category(new_name)
            print(f"Category with id {category_id} updated successfully.")
        except Exception as e:
            print(f"Error occurred: {e}")
    else:
        print(f"Category with id {category_id} does not exist")
    input("\nPress Enter to continue...")

def find_category_by_id():
    category_id = int(input("Enter category id: "))
    category = Category.get_category_by_id(category_id)
    if category:
        print(f"Category is: {category}")
    else:
        print(f"Category with id {category_id} does not exist")
    input("\nPress Enter to continue...")

def get_all_categories():
    categories = Category.get_all_categories()
    for category in categories:
        print(category)
    input("\nPress Enter to continue...")

def delete_category():
    category_id = int(input("Enter category id: "))
    try:
        Category.delete_category(category_id)
    except Exception as e:
        print(f"Error occurred: {e}")
    input("\nPress Enter to continue...")

def add_expense():
    amount = int(input("Enter amount: "))
    description = input("Enter description: ")
    user_id = int(input("Enter user ID: "))
    category_id = int(input("Enter category ID: "))
    try:
        Expense.create_expense(amount, description, user_id, category_id)
        print("Expense added successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")
    input("\nPress Enter to continue...")

def update_expense():
    expense_id = int(input("Enter expense id: "))
    expense = Expense.get_expense_by_id(expense_id)
    if expense:
        field = input("Enter field to update (amount, description, user_id, category_id): ")
        value = input(f"Enter new value for {field}: ")
        try:
            expense.update_expense(field, value)
            print(f"Expense with id {expense_id} updated successfully.")
        except Exception as e:
            print(f"Error occurred: {e}")
    else:
        print(f"Expense with id {expense_id} does not exist")
    input("\nPress Enter to continue...")

def find_expense_by_id():
    expense_id = int(input("Enter expense id: "))
    expense = Expense.get_expense_by_id(expense_id)
    if expense:
        print(f"Expense is: {expense}")
    else:
        print(f"Expense with id {expense_id} does not exist")
    input("\nPress Enter to continue...")

def get_all_expenses():
    expenses = Expense.get_all_expenses()
    for expense in expenses:
        print(expense)
    input("\nPress Enter to continue...")

def delete_expense():
    expense_id = int(input("Enter expense id: "))
    try:
        Expense.delete_expense(expense_id)
    except Exception as e:
        print(f"Error occurred: {e}")
    input("\nPress Enter to continue...")

def add_user():
    username = input("Enter username: ")
    email = input("Enter email: ")
    try:
        User.create_user(username, email)
        print("User added successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")
    input("\nPress Enter to continue...")

def update_user():
    user_id = int(input("Enter user id: "))
    user = User.get_user_by_id(user_id)
    if user:
        field = input("Enter field to update (username, email): ")
        value = input(f"Enter new value for {field}: ")
        try:
            user.update_user(field, value)
            print(f"User with id {user_id} updated successfully.")
        except Exception as e:
            print(f"Error occurred: {e}")
    else:
        print(f"User with id {user_id} does not exist")
    input("\nPress Enter to continue...")

def find_user_by_id():
    user_id = int(input("Enter user id: "))
    user = User.get_user_by_id(user_id)
    if user:
        print(f"User is: {user}")
    else:
        print(f"User with id {user_id} does not exist")
    input("\nPress Enter to continue...")

def get_all_users():
    users = User.get_all_users()
    for user in users:
        print(user)
    input("\nPress Enter to continue...")

def delete_user():
    user_id = int(input("Enter user id: "))
    try:
        User.delete_user(user_id)
    except Exception as e:
        print(f"Error occurred: {e}")
    input("\nPress Enter to continue...")


def exit_program():
    print("Goodbye!")
    exit()

