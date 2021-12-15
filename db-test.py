import mysql.connector

mydb = mysql.connector.connect(
    host = '10.200.0.17',
    user = 'flask_usr',
    passwd = 'Karantin14beetle',
    # auth_plugin='mysql_native_password'
)

my_cursor = mydb.cursor()

my_cursor.execute('show databases;')

for i in my_cursor:
    print(i)