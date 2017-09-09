import pyodbc

# config
server = 'hackrvce.database.windows.net'
database = 'dbrvce'
username = 'abhishek'
password = 'Password123'
driver= '{ODBC Driver 13 for SQL Server}'

# connection
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = cnxn.cursor()

cursor.execute("SELECT * FROM [dbo].[Table]")

row = cursor.fetchone()
while row:
    string = ""
    count = 0
    for i in row:
        string += str(row[count]) + "\t"
        count += 1
    print (string)
    row = cursor.fetchone()