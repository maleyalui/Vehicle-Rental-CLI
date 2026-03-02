#Only Admins Access decorators
# plus (Might also add a log for when users do something)
def admin_required(func):
    def wrapper(user):
        if user["role"] != "admin":
            print("Access denied! Admins only.")
            return
        return func(user)
    return wrapper