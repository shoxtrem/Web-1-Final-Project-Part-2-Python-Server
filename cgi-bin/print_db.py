#!/usr/bin/python3
# This script creates a database if one doesn't exist yet
# prints content of the database in a HTML table and prints the HTML page

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

# To save the changes in the files. Never skip this.
# If we skip this, nothing will be saved in the database.
connection.commit()

# execute the command to fetch all the data from the table directoryTable
crsr.execute("SELECT * FROM directoryTable")

# store all the fetched data in the ans variable
ans = crsr.fetchall()

print("Content-type: text/html; charset=utf-8\n")
html = """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Directory</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="/css/style.css">
  </head>
  <body>

    <!-- Navbar -->
    <div class="top">
      <div class="bar blue card left-align large">
        <ul>
          <li> <a href="/index.html">Home</a></li>
          <li class="dropdown"> <a href="javascript:void(0)" class="dropbtn">Display</a>
            <div class="dropdown-content">
              <a href="/cgi-bin/print_db.py">Full List</a>
              <a href="/search.html">Search</a>
            </div>
          </li>
          <li> <a href="/form.html">Add</a></li>
        </ul>
      </div>
    </div>

    <!-- Header -->
    <header class="container blue center" style="padding:128px 16px">
      <h1 class="margin jumbo">DISPLAY PAGE</h1>
      <p class="xlarge">Displaying all the names in the database</p>
    </header>

    <div class="row-padding padding-64 container">
      <div class="content">
        <div class="twothird">
          <h1>Members Array</h1>
          <h5 class="padding-32">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tdirectoryTableor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</h5>

            <p>
"""
html = html + """
<table class='table-all table' border='1'>"""
# Create a HTML Table with elements from the database.
# We also strip all the unecessary stuff like ('')
for row in ans:
    row = str(row).replace("('", "")
    row = row.replace("')", "")
    row = row.replace("', '", " ")
    html = html + """<tr><td>""" + row + """</td></tr>"""
html = html + """
</table>
</p>
</div>

<div class="third center">
<i class="fa fa-table padding-64 text-red"></i>
</div>
</div>
</div>
<!-- Footer -->
<footer class="container padding-64 center opacity">
<div class="xlarge padding-32">
  <i class="fa fa-facebook-official hover-opacity"></i>
  <i class="fa fa-instagram hover-opacity"></i>
  <i class="fa fa-snapchat hover-opacity"></i>
  <i class="fa fa-pinterest-p hover-opacity"></i>
  <i class="fa fa-twitter hover-opacity"></i>
  <i class="fa fa-linkedin hover-opacity"></i>
</div>
<p>Modified for WebDev Project</p>
</footer>

</body>
</html>
"""

# Print the HTML page
print(html)

# To save the changes in the files. Never skip this.
# If we skip this, nothing will be saved in the database.
connection.commit()

# Close connection to the database
connection.close()
