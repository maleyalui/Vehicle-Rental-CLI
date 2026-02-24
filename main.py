# Entry Point and menu sys

#Import dependancies
import getpass

#current_user = None

#Start menu

def start_menu():

#global current_user by adding global
#It makes current_user accessible in Start_menu()
    while True:
        print("--- Vehicle Rental System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter Choice: ")

        #Choice 1
        if choice == "1":
            Id = input("ID number: ")
            name = input("Nmae: ")
            password = getpass.getpass("Password: ")
            role = input("Role: ")
            
            #when role is empty automate user to customer
            if role == "":
                role = "customer"
            #Implement func to register from auth


        # Choice 2

        elif choice == "2":
            Id = input("ID number: ")
            password = getpass.getpass("Password: ")
            
            #Implement login func

            #If login successfull, give him correct menu

        
        elif choice == "3":
            print("Goodbye!")
            print("Exiting System")
            break
        else:
            print("Invalid choice.")


#The admin menu

#Pass the user
def admin_menu():
    while True:
        print("--- Admin Menu ---")
        print("1. Add Vehicle")
        print("2. List Vehicles")
        print("3. Logout")

        choice = input("Choice: ")

        if choice == "1":
            brand = input("Brand name: ")
            model = input("Model name: ")
            price = int(input("Price per day: "))
            #call  the func to add vehicle
        
        # elif choice == "2":
        #List vehicles

        elif choice == "3":
            print("Logging out...")
            break

        else:
            print("Invalid Choice")
            

#customer meu

#pass user from start_menu()

def customer_menu():
    while True:
        print("--- Customer Menu ---")
        print("1. List Vehicles")
        print("2. Rent Vehicle")
        print("3. Retturn Vehicle")
        print("4. Logout")

        choice = input("Enter Choice: ")

        #if choice == "1":
        #List the vehicles
        if choice == "2":
            vehicle_id = int(input("Vehicle ID: "))
            days = int(input("Enter days to rent (max 14): "))
            #call thefunc to rent
        
        elif choice == "3":
            vehicle_id = int(input("Vehicle ID: "))
            #the func to change status (return vehicle func)

        elif choice == "4":
            print("Logging Out...")
            break

        else:
            print("Invalid Choice. ")


#If main will be the entry point run start_menu()
if __name__ == "__main__":
    start_menu()