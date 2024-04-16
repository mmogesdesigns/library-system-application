import mysql.connector
from mysql.connector import Error
from connect_db import connect_db 

class Book:
    def __init__(self, title, author,isbn,genre,year_published) :
       self.title = title
       self.author = author
       self.isbn = isbn
       self.genre = genre
       self.year_published = year_published
       self.available = True

class Library:
    def __init__(self):
        self.books =[]

    def add_book(self):    
    
        try:

            conn = connect_db()
            cursor = conn.cursor()
      
            title=input(("Enter the title of the book: "))
            author=input(("Enter the auhtor of the book: "))
            isbn = input("Enter the ISBN of the book: ")
            genre=input(("Enter the genre of the book: "))
            year_published=input(("Enter the year the book was published: "))
            avavilability = True
            new_book = Book(title, author, isbn, genre, year_published)
            query = "INSERT INTO books (title, author_id, genre_id, isbn, publication_date, availability) VALUES (%s, %s, %s, %s, %s, %s)"

            cursor.execute(query, new_book)
            conn.commit()
            print("New book was succesfully added")


    
        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
        # close out the connection
            if conn.is_connected():
                cursor.close()
                conn.close()
            print("MySql connection closed")

           
        
    
    def borrow_book(self):
        try:
            # connecting to dc
            conn = connect_db()
            cursor = conn.cursor()
            
            
            isbn = input("Enter the ISBN of the book you want to borrow:\n")
            user_id = int(input("Enter your user ID: "))
            #********************* start here

            found_and_borrowed = False
            for book in self.books:
                if book.isbn == isbn:
                    if book.available:
                        book.available = False  
                        print(f"You have successfully borrowed '{book.title}'.")
                        found_and_borrowed = True
                    else:
                        print(f"The book '{book.title}' is currently not available for borrowing.")
                    break 

            if not found_and_borrowed:
           
                print("No book with that ISBN is available in the library.")
 
    
            another_book = input("Would you like to borrow another book? (yes/no)" )
            if another_book != 'yes':
               return  # Exit the function if user does not want to borrow another book
        except mysql.connector.Error as e:
            print(f"Error: {e}")
        except ValueError:
            print("Invalid input. Please enter correct data types.")
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
                print("MySQL connection closed")

    def return_book(self):
        isbn = input("Enter the ISBN of the book you are returning: \n")
        book_found = False
 
        for book in self.books:
            if book.isbn == isbn:
                book_found = True
                if not book.available:
                        book.available = True
                        print(f"Thank you for returning '{book.title}'.")
                        break
                else:
                    print(f"The book '{book.title}' was not borrowed.")
                break
        if not book_found:
                    print("No book with that ISBN is found in our library.")

       
            

    def search_book(self):
        while True:
            book_found = False
            isbn = input("Enter the ISBN of the book you want to search:\n")

            for book in self.books:
                if book.isbn == isbn:
                    status = "available" if book.available else "currently borrowed"
                    print(f"Book: '{book.title}' by: {book.author} {book.year} is {status} ")
                    book_found = True
                    break
            if not book_found:
                    print("Book not found! ")

    def display_all_books(self):
        if not self.books:
            print("There's currently no books in the library. ")
            return
        else:
            print("All Library Books: \n")
            for book in self.books:
                status = "available" if book.available else "currently borrowed"
                print(f"Book: '{book.title}' by: {book.author} - Status: {status} ")
             

def book_operations():
     library = Library()
     while True:
        print('\nBook Operations:')
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        try:
            book_operations_input = int(input("Please select one of the following options: "))

            if book_operations_input == 1:
                library.add_book()

            elif book_operations_input== 2:
                library.borrow_book()
                
            elif book_operations_input == 3:
                library.return_book()
        
            elif book_operations_input == 4:
                library.search_book()
            elif book_operations_input == 5:
                 library.display_all_books()

            
            else:
                print("Invalid option, please select a valid option. ")
        except Exception as e:
            print(f"Error: {e}")