# from book import Book, add_book, borrow_book, return_book, search_book, display_all_books

# Your main script code here

def user_operations():
    while True:
        print('\nUser Operations:')
        print("1. Add a new author")
        print("2. View user details")
        print("3. Display all users")
        try:
            user_operations_input = int(input("Please select one of the following options: "))

            if user_operations_input == 1:
                pass
       
            elif user_operations_input== 2:
                pass
        
            elif user_operations_input == 3:
                pass
        
            else:
                print("Invalid option, please select a valid option. ")
        except Exception as e:
            print(f"Error: {e}")
    
def author_operations():
    while True:
        print('\nAuthor Operations:')
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        try:
            author_operations_input = int(input("Please select one of the following options: "))

            if author_operations_input == 1:
                pass
       
            elif author_operations_input== 2:
                pass
        
            elif author_operations_input == 3:
                pass
        
            else:
                print("Invalid option, please select a valid option. ")
        except Exception as e:
            print(f"Error: {e}")
   




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
        # user_operations()
            elif menu_input == 3:
                pass
        # author_operations()
            elif menu_input == 4:
                print("Thank you for using the Library Management System. Goodbye!")
                break
            
            else:
                print("Invalid option, please select a valid option. ")
        except Exception as e:
            print(f"Error: {e}")



main_menu()