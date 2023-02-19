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


# import sqlite3
# sql = """
# DROP TABLE IF EXISTS People;
# CREATE TABLE People(
#     FirstName TEXT,
#     LastName TEXT,
#     Age INT
# );
# INSERT INTO People VALUES(
#     'Ron',
#     'Obvious',
#     '42'
# );"""
#
# with sqlite3.connect("test_database.db") as connection:
#     cursor = connection.cursor()
#     cursor.executescript(sql)

# import sqlite3
#
# #Get person data from user
#
# first_name = input("Enter your first name:")
# last_name = input("enter your last name:")
# age = int(input("Enter your age:"))
# data = (first_name,last_name,age)
#
#
# with sqlite3.connect("test_database.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute("INSERT INTO People VALUES(?,?,?);",data)
#     cursor.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?;",(45,'Lugi','Italioan'))

#RETRIEVING DATA

# import sqlite3
#
# values = (
#     ("Ron","Obvious",42),
#     ("Luigi","Vercotti",43),
#     ("Arthur","Belling",28)
# )
#
# with sqlite3.connect("test_database.db") as connection:
#     cursor = connection.cursor()
#     cursor.execute("DROP TABLE IF EXISTS People")
#     cursor.execute("""
#     CREATE TABLE People(
#         FirstName TEXT,
#         LastName TEXT,
#         Age INT
#         );"""
#     )
#     cursor.executemany("INSERT INTO People VALUES(?,?,?);",values)
#
#     #SELECT ALL FIRST AND LAST NAMES FROM PEOPLE OVER AGE 30
#     cursor.execute(
#         "SELECT FirstName,LastName FROM People WHERE Age > 30;"
#     )
#     for row in cursor.fetchall():
#         print(row)

#Review EXERCISES

#1
# import sqlite3
#
# with sqlite3.connect(":memory:") as connection:
#     c = connection.cursor()
#
#     c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, Age INT)")
#
#     #2
#     roster_data = (
#         ("Benjamin Sisko", "Human", 40),
#         ("Jadzia Dax", "Trill", 300),
#         ("Kira Nerys", "Bajoran", 29),
#     )
#     c.executemany("INSERT INTO Roster VALUES(?,?,?)",roster_data)
#
#     #3
#     c.execute(
#         "UPDATE Roster SET Name=? WHERE Name=?",("Ezri Dax", "Jadzia Dax")
#     )
#
#     #4
#     c.execute("SELECT Name, Age FROM Roster WHERE Species = 'Trill'")
#     for row in c.fetchall():
#         print(row)

#15.2 Libaries For Working With Other SQL Databases

