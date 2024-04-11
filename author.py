class Author:
    def __init__(self, name, author_id, biography) :
       self.name = name
       self.author_id = author_id
       self.biography = biography

class Authors:
    def __init__(self):
        self.authors ={}
        self.next_id = 1

    def add_author(self):
        name = input("Enter the author's name:")
        biography = input("Enter the author's biography: \n")

        author_id = str(self.next_id)
        new_author = Author(name, author_id,biography )
        self.authors[author_id]= new_author

        print(f"Author '{name}' added succesfully with the Library ID: {author_id}")
        self.next_id += 1

    def view_author_details(self):
        author_id = input("Enter the ID of the author you want to view: \n")

        if author_id in self.authors:
            author = self.authors[author_id]
            print(f"Author Information: \n")
            print(f"Name: '{author.name}'")
            print(f"Biography: {author.biography}")
            print(f"Author ID: '{author_id}'")
        else:
            print("No author found with that Author ID. ")

    def display_all_authors(self):
        if not self.authors:
            print("There's currently no authors.")
        
        else:
            for author_id, author in self.authors.items():
                print(f"Name: '{author.name}'")
                print(f"Biography: {author.biography}")
                print(f"author ID: {author_id}\n")










def author_operations(authors):
    while True:
        print('\nAuthor Operations:')
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        try:
            author_operations_input = int(input("Please select one of the following options: "))

            if author_operations_input == 1:
                authors.add_author()
       
            elif author_operations_input== 2:
                authors.view_author_details()
        
            elif author_operations_input == 3:
                authors.display_all_authors()
        
            else:
                print("Invalid option, please select a valid option. ")
        except Exception as e:
            print(f"Error: {e}")