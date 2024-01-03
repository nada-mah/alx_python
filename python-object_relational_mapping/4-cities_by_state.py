import MySQLdb
from sys import argv

mysql_username = argv[1]
mysql_password = argv[2]
mysql_database = argv[3]


dbconnect = MySQLdb.connect(host='localhost', port=3306, user=mysql_username, passwd=mysql_password, db=mysql_database)

cursor = dbconnect.cursor()

cursor.execute("SELECT * FROM cities ")
cities = cursor.fetchall()
for city in cities:
    print(city)

# Close all cursors
cursor.close()
# Close all databases
dbconnect.close()
