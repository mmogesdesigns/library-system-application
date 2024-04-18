from typing import Any
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
    def get_attributes(self) :
        return (self.title,self.author, self.isbn,self.genre, self.year_published, self.available)

class Library:
    def __init__(self):
        self.books =[]
        self.results= []

    def add_book(self):    
    
        try:

            conn = connect_db()
            cursor = conn.cursor()
      
            title=input(("Enter the title of the book: "))
            author=input(("Enter the auhtor of the book: "))
            isbn = input("Enter the ISBN of the book: ")
            genre=input(("Enter the genre of the book: "))
            year_published=input(("Enter the year the book was published: "))
            
            new_book = Book(title, author, isbn, genre, year_published)
            query = "INSERT INTO books (title, author_id, genre_id, isbn, publication_date, availability) VALUES (%s, %s, %s, %s, %s, %s)"

            cursor.execute(query, new_book.get_attributes())
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

            query = "SELECT availability FROM books WHERE isbn = %s"
            
            cursor.execute(query, isbn )
            result = cursor.fetchone()
           
            #********************* start here

            
            if result:
                if result == True:
                        query = "UPDATE books SET availability = false WHERE isbn = %s"
                        cursor.execute(query,isbn)
                        conn.commit() 
                        print(f"You have successfully borrowed '{book.title}'.")
                else:
                        print(f"The book '{book.title}' is currently not available for borrowing.")
                


            else:
                print("No book with that ISBN is available in the library.")
        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
        # close out the connection
            if conn.is_connected():
                cursor.close()
                conn.close()
            print("MySql connection closed")
 
         
    def return_book(self):
        try:
            # connecting to dc
            conn = connect_db()
            cursor = conn.cursor()
            isbn = input("Enter the ISBN of the book you are returning: \n")
            query = "SELECT availability FROM borrowed_books WHERE isbn =%s"

            cursor.execute(query, isbn )
            result = cursor.fetchone()
 
            if result:
                 if result == False:
                      query = "UPDATE books SET availability = true WHERE isbn = %s"
                      print(f"Thank you for returning '{book.title}'.")
                       
                 else:
                    print(f"The book '{book.title}' was not borrowed.")
                
            else:
                    print("No book with that ISBN is found in our library.")
        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
        # close out the connection
            if conn.is_connected():
                cursor.close()
                conn.close()
            print("MySql connection closed")
       
            

    def search_book(self):
        isbn = input("Enter the ISBN of the book you want to search:\n")
        try:
            conn = connect_db()
            cursor = conn.cursor()
            query ="SELECT title, author, genre, year_published, availability FROM books WHERE isbn =%s"
            cursor.execute(query,(isbn))
            result = cursor.fetchone()
            if result:
                    status = "available" if book.available else "currently borrowed"
                    print(f"Book: '{book.title}' by: {book.author} {book.year} is {status} ")
                    
            else:
                print("Book not found! ")

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
        # close out the connection
            if conn.is_connected():
                cursor.close()
                conn.close()
            print("MySql connection closed")

    def display_all_books(self):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            query = "SELECT * FROM books"
            cursor.execute(query)
            results = cursor.fetchall()
            self.results= results

            if results:
                print("All Library Books: \n")
            for book in self.books:
                status = "available" if book.available else "currently borrowed"
                print(f"Book: '{book.title}' by: {book.author} - Status: {status} ")
        
            else:
                print("There's currently no books in the library. ")

        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
        # close out the connection
            if conn.is_connected():
                cursor.close()
                conn.close()
            print("MySql connection closed")
     
            
             

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