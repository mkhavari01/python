from asyncio.windows_events import NULL
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="138131614Mahdi!",
  database="p1"
)
print("connection happent")
mycursor = mydb.cursor()
# mycursor2 = mydb.cursor()

username = input("Enter ur username: ")
password = input("Enter ur password: ")

sql = "INSERT INTO user (username, password) VALUES (%s, %s)"
val = (NULL, NULL)

mycursor.execute(sql,val)
mydb.commit()
# myresult = mycursor.fetchall()
# print(myresult)

# mycursor2.execute('insert info (name,weight,height) values ("new user",default,190)')
mydb.close()