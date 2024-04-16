from book import Book, Library, book_operations
from author import Author, Authors, author_operations
from user import User, Users, user_operations

def main_menu ():
    while True:
        print('\nWelcome to the Library Management System!')
        print('\nMain Menu:')
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")
        try:
            menu_input = int(input("Please select one of the following options: "))

            if menu_input == 1:
                book_operations()
            elif menu_input == 2:
                pass
                user_operations()
            elif menu_input == 3:
                pass
                author_operations()
            elif menu_input == 4:
                print("Thank you for using the Library Management System. Goodbye!")
                break
            
            else:
                print("Invalid option, please select a valid option. ")
        except Exception as e:
            print(f"Error: {e}")



if __name__ == "__main__":
    main_menu()