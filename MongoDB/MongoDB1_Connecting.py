from pymongo import MongoClient

# 1) Connect db using fn(): and return the function and use it.
def db_connecting():
    client = MongoClient('mongodb://localhost:27017')
    db = client['ABC']
    col = db['class 1']
    return col

connecting = db_connecting()

# 2) insertmany
insert_document = connecting.insert_many([{'Name':'Manikandan','RollNo':'001','Department':'CSC','CGPA':90.4},{'Name':'Mahendran','RollNo':'002','Department':'CSC','CGPA':88.84},{'Name':'Kathir','RollNo':'003','Department':'CSC','CGPA':86.8},{'Name':'Nikesh','RollNo':'004','Department':'CSC','CGPA':84.8},{'Name':'Govindraj','RollNo':'005','Department':'CSC','CGPA':81.0}])

# 3) find -> 003 Id document
Find_one_document= connecting.find_one({'RollNo':'002'})
print(Find_one_document)

# 4) Update -> Department "CSC" to "IT"
update_All_Document = connecting.update_many({'Department':'CSC'},{'$set':{'Department':'IT'}})
print(list(connecting.find()))

# 5) delete -> RollNO 004
# inser_one_rollno = connecting.insert_one({'Name':'Kathir','RollNo':'003','Department':'IT','CGPA':86.8})
count_Rollno = connecting.count_documents({'Department':'IT'})
print(count_Rollno)
delete_rollno = connecting.delete_one({'RollNo':'003'})
count_Rollno = connecting.count_documents({'Department':'IT'})
print(count_Rollno)
print(list(connecting.find()))



