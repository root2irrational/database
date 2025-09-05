import sqlite3

conn = sqlite3.connect('market.sqlite')
c = conn.cursor()
c.close()
