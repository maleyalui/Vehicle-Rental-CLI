#Handles User registration and login logic
# Import necessray dependancies
import json
import os
import hashlib
from models.users import User

USER_FILE = "data/users.json"

# func to Load users fom the Json files

def load_users():
#check if json exists if not return empty list/create new one
    if not os.path.exists(USER_FILE):
        #save users creates a dir and the file users.json
        save_users([])
        return []
    
    with open(USER_FILE, "r") as file:
        #Try loading the file
        try:
            return json.load(file)
        # if file is corrpt/broken overrite it with empty list 
        except json.JSONDecodeError: 
            print("Error: users.json file is corrupt. Resetted to empty! ")
            save_users([])
            return []

#Func to save Users to JSON file
def save_users(users):
    #Check if dir exists
    os.makedirs(os.path.dirname(USER_FILE), exist_ok=True)

    with open(USER_FILE, "w") as file:
        #save users
        json.dump(users,file,indent=4)

#Func to register

def register_user(id_no, name, password, role="customer"):
    #Check if ID exists
    users = load_users()

    for u in users:
        if u["id"] == id_no:
            print("Error: User already exists!")
            return None
    #Use User class to deal w naming    
    new_user = User(id_no,name,password,role)

    #convert new user to dict
    new_user_data = new_user.to_dict()

    #Add the data to load and save it
    users.append(new_user_data)
    save_users(users)

    print(f"--- Registration successful ---\n")
    print(f"Welcome {name}")

#Func to Login 
def login_user(id_no, password):
    users = load_users()
    #Check the hashed password
    #Hashed so as to compare with the users.py password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    for u in users:
        #See if user exists
        if u["id"] == id_no and u["password"] == hashed_password:
            print(f"Welcome back, {u['name']}!")
            return u
    
    print("Invalid ID or password!")
    return None
    

#if worka
#user1 = register_user("123456", "Luie 1", "Pass1")
#user2 = register_user("123455", "Luie 2", "Pass1")

# # Checks if user exists
#register_user("123456", "Luie 1", "Pass1")

# #To login
#login_user("123456", "Pass1")

# #wrong password
#login_user("123456", "12345")

#To see if it resets if file is corrupt
#load_users()

