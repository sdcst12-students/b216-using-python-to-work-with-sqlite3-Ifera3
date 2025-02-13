#!python

"""
Create a query to create a table to store pets information into a database for a veterinarian
Each record needs to have the following information:
id unique integer identifier
pet name
pet species (dog, cat)
pet breed (collie, beagle, persian, etc)
pet age
pet gender
pet neutered or spayed
owner ID

choose appropriate variable types for each field
create the database and add the following information. Make sure you commit the information to save it:
name            species         breed           age  gender     spayed/neutered?    ownerID
Fluffy          dog             Pomeraniam      5    m          true                101
Benjamin        cat             Siberian        8    m          true                103
Casey           cat             Siberian        8    m          true                103
Friend          cat             Domestic        4    m          false               102
Copper          dog             Beagle          12   m          true                104
"""

import sqlite3

file = 'dbase.db'
connection = sqlite3.connect(file)
cursor = connection.cursor()

query = '''
create table if not exists pets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TINYTEXT,
        species TINYTEXT,
        breed TINYTEXT,
        age INTEGER,
        gender TINYTEXT,
        neutered BOOLEAN,
        ownerID INTEGER);
'''
cursor.execute(query)

info = [['Fluffy','dog','Pomeraniam',5,'m',True,101],
    ['Benjamin','cat','Siberian',8,'m',True,103],
    ['Casey','cat','Siberian',8,'m',True,103],
    ['Friend','cat','Domestic',4,'m',False,102],
    ['Copper','dog','Beagle',12,'m',True,104]]
for i in info:
    query = f"insert into pets (name,species,breed,age,gender,neutered,ownerID) values ('{i[0]}','{i[1]}','{i[2]}',{i[3]},'{i[4]}',{i[5]},{i[6]});"
    #print(query)
    cursor.execute(query)

query = "select * from pets;"
cursor.execute(query)
result = cursor.fetchall()
print(result)

#connection.commit()