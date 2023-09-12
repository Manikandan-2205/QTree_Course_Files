from pymongo import MongoClient

# 1) Connect db using fn(): and return the function and use it.


def db_connecting():
    client = MongoClient('mongodb://localhost:27017')
    db = client['ABC']
    col = db['class 2']
    return col


connecting = db_connecting()

# 2) insert_many
insert_document = connecting.insert_many([{'Department': 'IT', 'Competition': 'Dance', 'Date': '10-09-202'}, {'Department': 'CS', 'Competition': 'Music', 'Date': '11-09-202'}, {'Department': 'CEE', 'Competition': 'Art', 'Date': '12-09-202'}, {'Department': 'ECE', 'Competition': 'MME', 'Date': '13-09-202'}, {'Department': 'Civil', 'Competition': 'Craft', 'Date': '14-09-202'}])
print(list(connecting.find()))

# 3) Update -> Department "CSC" to "IT"
# filter_doc = {"Department": "CS","Department": 'Civil',"Department":'IT'}
# update_doc = {"$set": {"Competition": "Music"}}
update_All_Document = connecting.update_one({"Department": 'IT'}, {"$set": {"Competition": "Music"}})
update_All_Document = connecting.update_one({"Department": 'CS'}, {"$set": {"Competition": "Music"}})
update_All_Document = connecting.update_one({"Department": 'Civil'}, {"$set": {"Competition": "Music"}})
print(list(connecting.find()))

# 4) delete -> RollNO 004
inser_one_rollno = connecting.insert_one(
    {'Department': 'Civil', 'Competition': 'Music', 'Date': '14-09-202'})
delete_rollno = connecting.delete_one({'Competition': 'Craft'})
print(list(connecting.find()))

# 5) insert_one 

insert_one_document = connecting.insert_one({'Department': 'AI & ML', 'Competition': 'PPT', 'Date': '13-09-202'})
print(list(connecting.find()))