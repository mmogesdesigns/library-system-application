import mysql.connector
from connect_db import connect_db

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

        try:
            conn = connect_db()
            cursor = conn.cursor()

            query = "INSERT INTO authors (name, biography)VALUES (%s,%s)"
            cursor.execute(query,(name,biography))
            conn.commit()
            print(f"Author '{name}' added successfully. ")
        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
        # close out the connection
            if conn.is_connected():
                cursor.close()
                conn.close()
            print("MySql connection closed")

    def view_author_details(self):
        author_id = input("Enter the ID of the author you want to view: \n") #****** ask about id or author_id
        try:
            conn = connect_db()
            cursor = conn.cursor()
            query = "SELECT name, biography FROM authors WHERE id = %s"
            cursor.execute(query,(author_id))
            result = cursor.fetchone()
            if result:
                print(f"Author Information: \nName: {result[0]}\nBiography: {result[1]}\nAuthor ID: {author_id}")

            else:
                print("No author found with that Author ID. ")
        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
        # close out the connection
            if conn.is_connected():
                cursor.close()
                conn.close()
            print("MySql connection closed")

    def display_all_authors(self):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            query = "SELECT * FROM authors"
            cursor.execute(query)
            results = cursor.fetchall()
            if results:
                print("All authors:")
                for author in results:
                    print(f"ID: {author[0]}, Name: {author[1]}, Biography: {author[2]}")
            else:
                print("There's currently no authors.")
        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
        # close out the connection
            if conn.is_connected():
                cursor.close()
                conn.close()
            print("MySql connection closed")


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