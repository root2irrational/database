
from db import userNameExists, initialiseDb, shutDownDb, registerUser, userPasswordMatch
from User import User
import numpy as np


def login():
    print("Enter your username: (should be 50 characters or less)")
    un: str = input()
    print("Enter your password: (should be 50 characters or less)")
    pw: str = input()
    user: User = User(un, pw)
    while (not user.loginValidate()):
        print("\nInvalid username or password\n")
        print("Enter your username: (should be 50 characters or less)")
        un: str = input()
        print("Enter your password: (should be 50 characters or less)")
        pw: str = input()
        user.setUserName(un)
        user.setPassword(pw)
    
    user.registerUser()
    return

def register():
    print("Enter your username: (should be 50 characters or less)")
    un: str = input()
    print("Enter your password: (should be 50 characters or less)")
    pw: str = input()
    user: User = User(un, pw)
    while (not user.registerValidate()):
        print("\nInvalid username or password\n")
        print("Enter your username: (should be 50 characters or less)")
        un: str = input()
        print("Enter your password: (should be 50 characters or less)")
        pw: str = input()
        user.setUserName(un)
        user.setPassword(pw)
    
    user.registerUser()
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



