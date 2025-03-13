import MySQLdb

dataBae = MySQLdb.connect(
    host="localhost",
    user="root",
    password="12345",
)

cursorObject = dataBae.cursor()
cursorObject.execute("CREATE DATABASE dcrm")

print("Database created successfully!!!!")
