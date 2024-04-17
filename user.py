import mysql.connector
from connect_db import connect_db
class User:
    def __init__(self, name, library_id) :
       self.name = name
       self.library_id = library_id
       

class Users:
    def __init__(self):# ************** ask if we need this
        self.results= []
        
    
    def add_user(self):
        name = input("Enter the user's name:")
        library_id = input("Enter the user's library ID: ")
        try:
            conn = connect_db()
            cursor = conn.cursor()
            query = "INSERT INTO users (name, library_id)"
            cursor.execute(query,(name,library_id))
            conn.commit()
            print(f"User: '{name}' added successfully with Library ID: {library_id}. ")
        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
        # close out the connection
            if conn.is_connected():
                cursor.close()
                conn.close()
            print("MySql connection closed")

    def view_user_details(self):
        library_id= input("Enter the Library ID of the user you want to view: \n")
        try:
            conn = connect_db()
            cursor = conn.cursor()
            query = "SELECT name, library_id FROM users WHERE library_id = %s"
            cursor.execute(query,(library_id))
            result = cursor.fetchone()
            if result:
                print(f"User Information: \nName:{result[0]}, Library ID: {result[1]}")
    

            else:
                print("No user found with that Library ID. ")
        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
        # close out the connection
            if conn.is_connected():
                cursor.close()
                conn.close()
            print("MySql connection closed")


    def display_all_users(self):
        try:
            conn = connect_db()
            cursor = conn.cursor()
            query = "SELECT id, name FROM users"
            cursor.execute(query)
            results = cursor.fetchall()
            self.results= results
           
            
            if results:
                print("All users:")
                for user in results:
                    print(f"ID: {user[0]}, Name:{user[1]}")
            else:
                print("There's currently no users.")
        except mysql.connector.Error as e:
            print(f"Error: {e}")

        finally:
        # close out the connection
            if conn.is_connected():
                cursor.close()
                conn.close()
            print("MySql connection closed")
        
       

    
def user_operations():
        users = Users()
        while True:
            print('\nUser Operations:')
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            try:
                user_operations_input = int(input("Please select one of the following options: "))

                if user_operations_input == 1:
                    users.add_user()
        
                elif user_operations_input== 2:
                    users.view_user_details()
            
                elif user_operations_input == 3:
                    users.display_all_users()
            
                else:
                    print("Invalid option, please select a valid option. ")
            except Exception as e:
                print(f"Error: {e}")