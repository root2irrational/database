
from db import userNameExists, initialiseDb, shutDownDb, registerUser, userPasswordMatch
import numpy as np

    
def register():
    unInvalid: bool = True
    firstTime: bool = True
    un: str = None
    while (unInvalid):
        if firstTime:
            print( 
                    """
                    To make a new account, 
                    Enter user name (max limit is 50 characters):
                    """
                )
            firstTime = False
        else:
            print( 
                    """
                    Invalid user name or username already exists, 
                    Enter user name (max limit is 50 characters):
                    """
                )
        un = input()
        unInvalid =  (len(un) > 50 or userNameExists(un))
        
    pw: str = None
    unInvalid: bool = True
    firstTime: bool = True
    while (unInvalid):
        if firstTime:
            print( 
                    """
                    To make a new account, 
                    Enter password (max limit is 50 characters):
                    """
                )
            firstTime = False
        else:
            print( 
                    """
                    Invalid password,
                    Enter password (max limit is 50 characters):
                    """
                )
        pw = input()
        unInvalid = (len(pw) > 50)
    registerUser(un, pw)
    return

def login():
    unInvalid: bool = True
    firstTime: bool = True
    un: str = None
    while (unInvalid):
        if firstTime:
            print( 
                    """
                    To Login, 
                    Enter user name (max limit is 50 characters):
                    """
                )
            firstTime = False
        else:
            print( 
                    """
                    Invalid user name or username already exists, 
                    Enter user name (max limit is 50 characters):
                    """
                )
        un = input()
        unInvalid = not userNameExists(un)
        
    pw: str = None
    unInvalid: bool = True
    firstTime: bool = True
    while (unInvalid):
        if firstTime:
            print( 
                    """
                    To Login, 
                    Enter password:
                    """
                )
            firstTime = False
        else:
            print( 
                    """
                    Invalid password, 
                    Enter password:
                    """
                )
        pw = input()
        unInvalid = not userPasswordMatch(un, pw)
    return

def main():
    initialiseDb()
    print(
            """
            Welcome to the slave market!\n
            Please login or register to use our services.\n
            Type l to login or r to register\n
            """
        )
    c = input()
    if c == "l":
        login()
        print("login success!")
    elif c == "r":
        register()
        print("registration success!")
    
    shutDownDb()
    
    return

if __name__ == "__main__":
    main()



