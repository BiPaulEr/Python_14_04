import os

directory = os.path.dirname(__file__)
file_name = "db.db"
path = os.path.join(directory, file_name)

import sqlite3

conn = sqlite3.connect(path)

cursor = conn.cursor()
"""
cursor.execute( "" CREATE TABLE employees (
                    id INTEGER PRIMARY KEY,
                    name VARCHAR(20),
                    balance DECIMAL(6, 2)
               )
               "")

cursor.execute( "" INSERT INTO employees (name, balance) VALUES ('DUPONT', 200)
               "")
"""
"""
cursor.executemany("INSERT INTO employees (name, balance) VALUES (?, ?)",
    [('MARTIN', 4200), ('LEFEVBRE', 3000), ('AIGOUYI', -200)]
)

conn.commit()
"""
"""
cursor.execute( "" SELECT * FROM employees"")
for row in cursor.fetchall():
    print(row)
"""

def getEmployees(cursor, balance_montant, operator = "<"):
    cursor.execute( f"SELECT * FROM employees WHERE balance {operator} {balance_montant}")
    for row in cursor.fetchall():
        print(row)

getEmployees(cursor, 4000)

cursor.close()

conn.close()
