import pyodbc
import os
import sys
import datetime

# config
server = 'hackrvce.database.windows.net'
database = 'dbrvce'
username = 'abhishek'
password = 'Password123'
driver= '{ODBC Driver 13 for SQL Server}'

USN = sys.argv[1]

query = "INSERT INTO [dbo].[Table] (USN) VALUES ('" + USN + "')"
print(query)

# connection
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = cnxn.cursor()

cursor.execute(query)
cursor.commit()