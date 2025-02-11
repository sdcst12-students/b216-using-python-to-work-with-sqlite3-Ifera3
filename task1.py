#!python

"""
Create a query to create a table to store customers information into a database for a veterinarian
Each record needs to have the following information:
id unique integer identifier
owner name
owner email
owner phone number
owner customer identification number
owner address
owner balance owing

choose appropriate variable types for each field
create the database and add the following information. Make sure you commit the information to save it:
name            email           phone number    ID      address                 balance
Joe Smith       joe@gmail.com   7783341111      101     1234 Sesame Street      0
Fred Jones      fred@city.com   6045553434      102     75 57 Street            0
Leroy Jenkins   leroy@wow.ca    2342222323      103     65 Blizzard Ave         100     
Jen Mezei       jen@shaw.ca     6042231134      104     891 Cullen Cresc        0
"""

import sqlite3

file = 'dbase.db'
connection = sqlite3.connect(file)
cursor = connection.cursor()

query = '''
create table if not exists customerInformation (
    id INTEGER PRIMARY KEY autoincrement,
    name tinytext,
    email tinytext,
    phoneNumber int,
    custumerID int,
    address tinytext,
    balance int);
'''
cursor.execute(query)

information = [
    ['Joe Smith','joe@gmail.com',7783341111,101,'1234 Sesame Street',0],
    ['Fred Jones','fred@city.com',6045553434,102,'75 57 Street',0],
    ['Leroy Jenkins','leroy@wow.ca',2342222323,103,'65 Blizzard Ave',100],
    ['Jen Mezei','jen@shaw.ca',6042231134,104,'891 Cullen Cresc',0]]
for i in information:
    query = f"insert into customerInformation (name,email,phoneNumber,custumerID,address,balance) values ('{i[0]}','{i[1]}',{i[2]},{i[3]},'{i[4]}',{i[5]});"
    cursor.execute(query)

query = "select * from customerInformation;"
cursor.execute(query)
result = cursor.fetchall()
print(result)
