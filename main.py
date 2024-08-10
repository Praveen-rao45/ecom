import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Praveen@123", database="revamp_academy")

mycursor=mydb.cursor()
mycursor.execute("select*from students")
for i in mycursor:
    print(i)