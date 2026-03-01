# calls the register user and login user from user_services

#Import Dependancies
from services.users_services import register_user, login_user
#Register
def register_user(id_no, name, password, role="customer"):
    return register_user(id_no, name, password, role)
#Login
def login_user(id_no, password):
    return login_user(id_no, password)
