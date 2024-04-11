class User:
    def __init__(self, name, library_id, birthday) :
       self.name = name
       self.library_id = library_id
       self.birthday = birthday

class Users:
    def __init__(self):
        self.users ={}
        self.next_id = 1
    
    def add_user(self):
        name = input("Enter the user's name:")
        birthday = input("Enter the user's birthday (YYYY-MM-DD): \n")

        library_id = str(self.next_id)
        new_user = User(name, library_id, birthday)
        self.users[library_id] = new_user

        print(f"User '{name}' added succesfully with the Library ID: {library_id}")
        self.next_id += 1

    def view_user_details(self):
        library_id= input("Enter the Library ID of the user you want to view: \n")
    
        if library_id in self.users:
            user = self.users[library_id]
            print(f"User Information: \n")
            print(f"Name: '{user.name}'")
            print(f"Birthday: '{user.birthday}'")
            print(f"Library ID: '{library_id}'")
        else:
            print("No user found with that Library ID. ")

    def display_all_users(self):
        if not self.users:
            print("There's currently no users.")
        
        else:
            print("Showing all users:\n")
            for library_id, user in self.users.items():
                print(f"Name: '{user.name}'")
                print(f"Birthday: '{user.birthday}'")
                print(f"Library ID: {library_id}\n")


    
def user_operations(users):
        while True:
            print('\nUser Operations:')
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            try:
                user_operations_input = int(input("Please select one of the following options: "))

                if user_operations_input == 1:
                    users.add_user(users)
        
                elif user_operations_input== 2:
                    users.view_user_details(users)
            
                elif user_operations_input == 3:
                    users.display_all_users(users)
            
                else:
                    print("Invalid option, please select a valid option. ")
            except Exception as e:
                print(f"Error: {e}")