import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = ""
)

#preparing a cursor object to help us make connection to the database
cursorObject = dataBase.cursor()

#creating the database using the cursor

cursorObject.execute("CREATE DATABASE CRM")

print("All done !!")