# calls the register user and login user from user_services

#Import Dependancies
from services import users_services
#Register
def register_user(id_no, name, password, role="customer"):
    return users_services.register_user(id_no, name, password, role)
#Login
def login_user(id_no, password):
    return users_services.login_user(id_no, password)
