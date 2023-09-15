import mysql.connector
# import getpass

# user = input("Enter your user name:")
# paw = getpass.getpass("Enter your password:")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="money",
    database="Student"
)

mycursor = mydb.cursor()
# print("database connecting to the mysql")
# 1) Create a DataBase
# mycoursor.execute("CREATE DATABASE Student")


# 2) Create a Table
# mycursor.execute("CREATE TABLE stu_record(Name Varchar(50) Not null, Roll_No int(5),Department Varchar(10), CGPA Varchar(5))")

# 3) Insert many record
# sql = "INSERT INTO stu_record (Name, Roll_No, Department, CGPA) VALUES (%s, %s, %s, %s)"
# val = [
#     ('Manikandan', 1001, 'CSC', 90.4),
#     ('Mahendran', 1002, 'CSC', 88.9),
#     ('Kathir', 1003, 'CSC', 86.4),
#     ('Nikesh', 1004, 'CSC', 82.7),
#     ('Govindraj', 1005, 'CSC', 80.4)
# ]

# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "rows were inserted.")

#  4) SHOW Roll no 1002 records

# mycursor.execute("select * from stu_record")
# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

# 5) Modify the record

mycursor.execute("UPDATE stu_record SET Department='CS' WHERE Name= 'Manikandan';")
mydb.commit()

mycursor.execute("select * from stu_record")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

