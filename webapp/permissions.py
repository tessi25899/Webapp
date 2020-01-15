from .models import *

#Alle RollenIDs
ROLE_ADMIN = 1
ROLE_BETREUERTEAM = 2
ROLE_STADTJUGENDWART = 3
ROLE_USER = 4

def UserAdmin(user):
    if user.role.id == ROLE_ADMIN:
        print("Admin")
        return True
    else:
        print("kein Admin")
        return False