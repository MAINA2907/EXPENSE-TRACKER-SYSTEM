# lib/cli.py
from database.setup import create_tables 
from helpers import (
    exit_program,
    add_category,
    update_category,
    find_category_by_id,
    get_all_categories,
    delete_category,
    add_expense,
    update_expense,
    find_expense_by_id,
    get_all_expenses,
    delete_expense,
    add_user,
    update_user,
    find_user_by_id,
    get_all_users,
    delete_user
)


def main():
    
    create_tables()
    while True:

        menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_category()
        elif choice == 2:
            update_category()
        elif choice == 3:
            find_category_by_id()
        elif choice == 4:
            get_all_categories()
        elif choice == 5:
            delete_category()
        elif choice == 6:
            add_expense()
        elif choice == 7:
            update_expense()
        elif choice == 8:
            find_expense_by_id()
        elif choice == 9:
            get_all_expenses()
        elif choice == 10:
            delete_expense()
        elif choice == 11:
            add_user()
        elif choice == 12:
            update_user()
        elif choice == 13:
            find_user_by_id()
        elif choice == 14:
            get_all_users()
        elif choice == 15:
            delete_user()
        elif choice == 16:
            exit_program()
        else:
            print("Invalid choice.")
        


def menu():
    print("Please select an option:")
    print("1. Add Category")
    print("2. Update Category")
    print("3. Find Category by ID")
    print("4. Get All Categories")
    print("5. Delete Category")
    print("6. Add Expense")
    print("7. Update Expense")
    print("8. Find Expense by ID")
    print("9. Get All Expenses")
    print("10. Delete Expense")
    print("11. Add User")
    print("12. Update User")
    print("13. Find User by ID")
    print("14. Get All Users")
    print("15. Delete User")
    print("16. Exit")


if __name__ == "__main__":
    main()
