from db import conn, c

class User:
    
    def __init__(self, userName: str, password: str):
        self.__userName = userName
        self.__password = password
        return
    
    def setUserName(self, userName: str):
        self.__userName = userName
        return
    
    def setPassword(self, password: str):
        self.__password = password
        return
    
    def registerValidate(self) -> bool:
        un: str = self.__userName
        pw: str = self.__password
        
        c.execute(
            """
            SELECT COUNT(userName)
            FROM users
            WHERE userName = ?;
            """,
            (un,)
        )
        usernameDoesNotExist: bool = not c.fetchone()[0] > 0
        usernameLengthValid: bool = not (len(un) > 50)
        passowrdLengthValid: bool = not (len(pw) > 50)
        return usernameDoesNotExist and usernameLengthValid and passowrdLengthValid
    
    def loginValidate(self) -> bool:
        un: str = self.__userName
        pw: str = self.__password
        c.execute(
            """
            SELECT COUNT(*)
            FROM users
            WHERE userName = ? AND password = ?;
            """,
            (un, pw)
        )
        loginValid: bool = c.fetchone()[0] == 1
        return loginValid
    
    def registerUser(self):
        un: str = self.__userName
        pw: str = self.__password
        c.execute(
                """
                INSERT INTO users (userName, password)
                VALUES (?, ?);
                """,
                (un, pw)
            )
        conn.commit()
        return