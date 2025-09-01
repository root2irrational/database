import sqlite3

conn = sqlite3.connect('data.sqlite')
db = conn.cursor()

db.execute('''
CREATE TABLE IF NOT EXISTS users (
    userId INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    deposit DECIMAL(18,4),
    portfolio DECIMAL(18,4),
)
''')

db.execute('''
CREATE TABLE IF NOT EXISTS Orders (
    orderId INTEGER PRIMARY KEY,
    userId INTEGER UNIQUE,
    instId INTEGER,
    side ENUM('BUY','SELL'),
    price DECIMAL(18,4),
    quantity DECIMAL(18,4),
    status ENUM('OPEN','FILLED','CANCELLED'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
)
''')

db.execute('''
CREATE TABLE Trades (
    tradeId INTEGER PRIMARY KEY,
    buy_order_id INTEGER,
    sell_order_id INTEGER,
    instrument_id INTEGER,
    price DECIMAL(18,4),
    quantity DECIMAL(18,4),
    tradeTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (buy_order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (sell_order_id) REFERENCES Orders(order_id)
);
''')

def addUser(userName: str, deposit: float, portfolio: float):
    user = [userName, deposit, portfolio]
    db.executemany('INSERT INTO users (userName, deposit, portfolio) VALUES (?, ?, ?)', user)
    return

conn.commit()

db.execute(
    ''' 
    SELECT * FROM users
    ''')

rows = db.fetchall()
for row in rows:
    print(row)


conn.close()
