
import sqlite3


conn = sqlite3.connect('market.sqlite')
c = conn.cursor()

def initialiseDb():
    c.execute("PRAGMA foreign_keys = ON")
    conn.commit()

    c.execute(
        """
        CREATE TABLE IF NOT EXISTS users(
            userId INTEGER PRIMARY KEY,
            userName VARCHAR(255),
            password VARCHAR(255)
        );
        """
    )
    conn.commit()
    
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS transactions(
            transactionId INTEGER PRIMARY KEY,
            userId INTEGER,
            amount INTEGER,
            FOREIGN KEY (userId) REFERENCES users(userId)
        );
        """
    )
    conn.commit()
    
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS instruments(
            instrumentId INTEGER PRIMARY KEY,
            ticker VARCHAR(255)
        );
        """
    )
    conn.commit()
    
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS portfolios(
            portfolioId INTEGER PRIMARY KEY,
            userId INTEGER,
            instrumentId INTEGER,
            avgPrice DECIMAL,
            FOREIGN KEY (userId) REFERENCES users(userId),
            FOREIGN KEY (instrumentId) REFERENCES instruments(instrumentId)
        );
        """
    )
    conn.commit()
    
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS portfoliosReturns(
            returnId INTEGER PRIMARY KEY,
            portfolioId INTEGER,
            date DATETIME,
            dailyReturn DECIMAL,
            cumulativeReturn DECIMAL,
            FOREIGN KEY (portfolioId) REFERENCES portfolios(portfolioId)
        );
        """
    )
    conn.commit()
    
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS orders(
            orderId INTEGER PRIMARY KEY,
            userId INTEGER,
            date DATETIME,
            orderType VARCHAR(255),
            status VARCHAR(255),
            price DECIMAL,
            quantity DECIMAL,
            FOREIGN KEY (userId) REFERENCES users(userId)
        );
        """
    )
    conn.commit()
    
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS trades(
            tradeId INTEGER PRIMARY KEY,
            orderId1 INTEGER,
            orderId2 INTEGER,
            date DATETIME,
            orderType VARCHAR(255),
            priceFilled DECIMAL,
            quantityFilled DECIMAL,
            FOREIGN KEY (orderId1) REFERENCES orders(orderId1)
            FOREIGN KEY (orderId2) REFERENCES orders(orderId2)
        );
        """
    )
    conn.commit()
    
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS prices(
            priceId INTEGER PRIMARY KEY,
            instrumentId INTEGER,
            date DATETIME,
            price DECIMAL,
            volume DECIMAL,
            FOREIGN KEY (instrumentId) REFERENCES instruments(instrumentId)
        );
        """
    )
    conn.commit()
    
    return

def userNameExists(s: str) -> bool:
    c.execute(
            """
            SELECT COUNT(userName)
            FROM users
            WHERE userName = ?;
            """,
            (s,)
        )
    
    count = c.fetchone()[0]
    return count > 0

def registerUser(un: str, pw: str):
    c.execute(
            """
            INSERT INTO users (userName, password)
            VALUES (?, ?);
            """,
            (un, pw)
        )
    conn.commit()
    return

def userPasswordMatch(un: str, pw: str) -> bool:
    c.execute(
            """
            SELECT COUNT(*)
            FROM users
            WHERE userName = ? AND password = ?;
            """,
            (un, pw)
        )
    
    count = c.fetchone()[0]
    return count == 1

def shutDownDb():
    c.close()

