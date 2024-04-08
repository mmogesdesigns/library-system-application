class Book:
    def __init__(self, title, author,isbn,genre,year_published) :
       self.title = title
       self.author = author
       self.isbn = isbn
       self.genre = genre
       self.year_published = year_published
       self.available = True

def book_operations():
     books =[]
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
                add_book(books)

            
            elif book_operations_input== 2:
                
                borrow_book(books)
                
    
            elif book_operations_input == 3:
                pass
        # author_operations()
            elif book_operations_input == 4:
                pass
            elif book_operations_input == 5:
                pass
            
            else:
                print("Invalid option, please select a valid option. ")
        except Exception as e:
            print(f"Error: {e}")
    
def add_book(books):
    while True:
        print('\nBook Operations:')
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
       

        try:
                title=input(("Enter the title of the book: "))
                author=input(("Enter the auhtor of the book: "))
                isbn = input("Enter the ISBN of the book: ")
                genre=input(("Enter the genre of the book: "))
                year_published=input(("Enter the year the book was published: "))
                
                
                new_book = {
                    "title": title,
                    "author":author,
                    'ISBN': isbn,
                    'genre': genre,
                    'year_published': year_published,
                    
                }
            
                books.append(new_book)
                print(f"n\'{new_book['title']}' has been added successfully!")
        except Exception as e:
            print(f"Error: {e}")
    
def borrow_book():
    pass