import sqlite3

conn = sqlite3.connect('data.sqlite')
db = conn.cursor()

db.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    rank INTEGER,
    balance REAL
)
''')

users_data = [
    ('Black', 1, 10.81),
    ('Nigger balls', 1, 11.00),
    ('Inside diddy', 1, 14.00)
]

db.executemany('INSERT INTO users (name, rank, balance) VALUES (?, ?, ?)', users_data)

conn.commit()

db.execute(
    ''' 
    SELECT * FROM users
    ''')

rows = db.fetchall()
for row in rows:
    print(row)


conn.close()
