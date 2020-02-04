from users.models import *
from profiles.models import *

#Alle GruppenIDs
GROUP_STADT = 1
GROUP_AKTIVE = 2
GROUP_JUGEND = 3
GROUP_UNTERSTÜTZUNG = 4
GROUP_ALTERABTEILUNG = 5

#Alle RollenIDs
ROLE_LEITER = 1
ROLE_STADTJUGENDWART = 2
ROLE_EINHEITSFUEHRUNG = 3
ROLE_JUGENDWART = 4
ROLE_BETREUERTEAM = 5

def get_current_user(user):
    try:
        users = Profile.objects.get(username=user.id)
    except:
        users = None
    return users

def check_user(user):
    current_user = get_current_user(user)
    if not current_user == None:
        print(current_user)
        return True
    else:
        print("Kein User")
        return False

#Alle mit der Role: ADMIN, STADTJUGENDWART, LEITER
def check_admin(user):
    current_user = get_current_user(user)
    if not current_user == None:
        if current_user.admin == True or current_user.role.id == ROLE_STADTJUGENDWART or current_user.role.id == ROLE_LEITER:
            print("Admin")
            return True
        else:
            print("Kein Admin")
            return False

#Alle mit der Role: ADMIN, STADTJUGENDWART, LEITER, JUGENDWART
def check_jugendwart(user):
    if check_admin(user) == False:   
        current_user = get_current_user(user)
        if not current_user == None:
            if current_user.role.id == ROLE_JUGENDWART:
                print("Jugendwart")
                return True
            else:
                print("Kein Jugendwart")
                return False
    else:
        return True

#Alle mit der Role: ADMIN, STADTJUGENDWART, LEITER, JUGENDWART, BETREUERTEAM
def check_betreuerteam(user):
    if check_einheitsfueher(user) == False:
        if check_jugendwart(user) == False:
            if check_admin(user) == False:   
                current_user = get_current_user(user)
                if not current_user == None:
                    if current_user.role.id == ROLE_BETREUERTEAM:
                        print("Betreuer")
                        return True
                    else:
                        print("Kein Betreuer")
                        return False
            else:
                return True
    else:
        return True

#Alle mit der Role: ADMIN, STADTJUGENDWART, LEITER, EINHEITSFUEHRUNG
def check_einheitsfueher(user):
    if check_admin(user) == False:   
        current_user = get_current_user(user)
        if not current_user == None:
            if current_user.role.id == ROLE_EINHEITSFUEHRUNG:
                print("Einheitsführer")
                return True
            else:
                print("Kein Einheitsführer")
                return False
    else:
        return True