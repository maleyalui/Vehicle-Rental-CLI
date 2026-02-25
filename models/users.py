#Has user and person classes

#haslib is used for encrypting passwords
#Might also use getpass to hide passowrds while typing
import hashlib

class Person:
    def __init__(self, name):
        self._name = name # Name is set to a private attribute but not enforced

    @property
    def name(self):
        return self._name
    
    #Code will still work since the setter is not required

    # @name.setter
    # def name(self, value):
    #     if not value:
    #         raise ValueError("Name cannot be Empty")
    #     self._name = value

class User(Person):
    id_counter = 1

    ##--------------------------##
    ##---Write your code here---##

    def __init__(self, id_no,name, password, role = "customer"):
        super().__init__(name) # User inherits from Person class

    #ID should be unique identifier and role
        self.id = id_no
    #Role is  'customer' by default unless otherwise
        self.role = role
    #Use Hashlib for security- we use SHA-256 hash for safety
    #.encode() turns string to bytes and sha256 hashes it and hexdigest makes the hashed to a string
        self._password = hashlib.sha256(password.encode()).hexdigest()
    #Check Password
    
    #Create a dictionary for Json storage

    def to_dict(self):

        return{
            "id": self.id,
            "name":self.name,
            "password":self._password,
            "role": self.role
        }
    
#if it works

#Luie = User("1144693","Luie Maleya", "1234")
#print(f"Hello {Luie.name} your account with id:{Luie.id} has been created")
# print(f"the json file is: {Luie.to_dict()}")