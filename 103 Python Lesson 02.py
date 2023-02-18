# import sqlite3
# connection = sqlite3.connect("test_database.db")
# print(type(connection))
#
# cursor = connection.cursor()
# print(type(cursor))
#
# query ="SELECT datetime('now','localtime');"
# results = cursor.execute(query)
# print(results)
# row = results.fetchone()
# print(row)
# time =row[0]
# print(time)
# connection.close()

#USING WITH TO MANAGE YOUR DATABASE CONNECTION

# with sqlite3.connect("test_database.db") as connection:
#     cursor = connection.cursor()
#     query = "SELECT datetime('now','localtime');"
#     results = cursor.execute(query)
#     row = results.fetchone()
#     time = row[0]
# print(time)

#WORKING WITH DATABASE TABLES

# create_table = """
# CREATE TABLE People(
#     FirstName TEXT,
#     LastName TEXT,
#     Age INT
#     );"""
# insert_values ="""
# INSERT INTO People VALUES(
#     'Ron',
#     'Obvious',
#     42
# );"""
#
# connection = sqlite3.connect("test_database.db")
# cursor = connection.cursor()
# # cursor.execute(create_table)
# cursor.execute(insert_values)
# connection.commit()
# connection.close()
#
# connection = sqlite3.connect("test_database.db")
# cursor = connection.cursor()
# query = "SELECT * FROM People;"
# results = cursor.execute(query)
# fetch = results.fetchone()
# print(fetch)



# create_table = """
# CREATE TABLE People(
#     FirstName TEXT,
#     LastName TEXT,
#     Age INT
#     );"""
# insert_values ="""
# INSERT INTO People VALUES(
#     'Ron',
#     'Obvious',
#     42
# );"""
#
# with sqlite3.connect("test_database.db") as connection:
#     cursor = connection.cursor()
#     # cursor.execute(create_table)
#     cursor.execute(insert_values)


import sqlite3
sql = """
DROP TABLE IF EXISTS People;
CREATE TABLE People(
    FirstName TEXT,
    LastName TEXT,
    Age INT
);
INSERT INTO People VALUES(
    'Ron',
    'Obvious',
    '42'
);"""

with sqlite3.connect("test_database.db") as connection:
    cursor = connection.cursor()
    cursor.executescript(sql)
