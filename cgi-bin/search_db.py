#!/usr/bin/python3
# This script creates a database if one doesn't exist yet
# uses user input to search said database for a string
# prints the result of said search in a HTML table and prints the HTML page

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

# Store form data and turn into Strings add joker character
form = cgi.FieldStorage()
search = str(form.getvalue("search"))
search = '%' + search + '%'

# SQL command to check if the search querry is in any of the columns
crsr.execute(
    "SELECT * FROM directoryTable WHERE ( fname || ' ' || lname LIKE (?) )", (search,))

# Get all the rows and columns everything!!!
searchResult = crsr.fetchall()

print("Content-type: text/html; charset=utf-8\n")


html = """<!DOCTYPE html>
<html>
<title>Directory</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<link rel="stylesheet" type="text/css" href="/css/style.css">

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
    <h1 class="margin jumbo">SEARCH PAGE</h1>
    <p class="xlarge">Enter the name you wish to search</p>
  </header>

<!-- Form with pattern to only allow text characters and spaces, prevent SQL injections-->
        <form autocomplete="on" action="/cgi-bin/search_db.py" method="post">
          Search the Database: <input type="search" id="search" pattern="^[a-zA-Zàâçéèêëîïôûùüÿñæœ ]*$" name="search"><br>
          <div class="button">
            <button id="submitQuerry" type="submit">Submit</button>
          </div>
        </form>

<div class="row-padding padding-64 container">
  <div class="content">
    <div class="twothird"><p>
"""
html = html + """
<table class='table-all table' border='1'>"""
# Create a HTML Table with elements from the database.
# We also strip all the unecessary stuff like ('')
for row in searchResult:
    row = str(row).replace("('", "")
    row = row.replace("')", "")
    row = row.replace("', '", " ")
    html = html + """<tr><td>""" + row + """</td></tr>"""
html = html + """
</table>
</p>
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
