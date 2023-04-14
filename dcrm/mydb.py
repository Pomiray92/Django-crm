"""
Install Mysql on comp
https://dev.mysql.com/downloads/installer/
pip install mysql
pip install mysql-connector
oder
pip install mysql-connector-python
"""

import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password",
    
    )

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE crm_db")

print("Nice DB is created")