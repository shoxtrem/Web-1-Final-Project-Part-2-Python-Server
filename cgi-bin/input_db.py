#!/usr/bin/python3
# This script creates a database if one doesn't exist yet
# uses user input to populate said database

# importing the module
import cgi
import sqlite3

# Connect or create the database
connection = sqlite3.connect("directoryDatabase.db")

# cursor
crsr = connection.cursor()

# SQL command to create a table in the database
sql_command = """CREATE TABLE directoryTable (
fname VARCHAR(20),
lname VARCHAR(30));"""

# execute the statement if the table exists and the database
tb_exists = "SELECT name FROM sqlite_master WHERE type='table' AND name='directoryTable'"
if not crsr.execute(tb_exists).fetchone():
    crsr.execute(sql_command)

# Store form data and turn into Strings, store in variables
form = cgi.FieldStorage()
name = str(form.getvalue("name"))
lastname = str(form.getvalue("lastname"))

# SQL command to insert the data in the table
crsr.execute(
    "INSERT INTO directoryTable (fname, lname) VALUES (?, ?)", (name, lastname))


# To save the changes in the files. Never skip this.
# If we skip this, nothing will be saved in the database.
connection.commit()

# Close connection to the database
connection.close()

# Open HTML file, read it assign it to a variable and close it then print it
# TODO: Add confirmation message
file = open('form.html')
html = file.read()
file.close()
print(html)
