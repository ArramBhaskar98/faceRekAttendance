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

now = datetime.datetime.now()
curHour = now.hour
curPeriod = curHour - 8

query = "UPDATE [dbo].[Table] SET Att" + str(curPeriod) + " = 1 WHERE USN='" + USN + "'"
print(query)

# connection
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = cnxn.cursor()

cursor.execute(query)
cursor.commit()