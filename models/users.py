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

    #ID should be unique identifier

    #Use Hashlib for security

    #Check Password
    
    #Create a dictionary for Json storage