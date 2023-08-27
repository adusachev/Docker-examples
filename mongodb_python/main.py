from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.son import SON

client = MongoClient("mongodb://root:pass@localhost:27019/")

db = client.testdb  # create db
people = db.people  # create collection

# insert data
mike_id = people.insert_one({"name": "Mike", "age": 30}).inserted_id  # return ObjectId
people.insert_one({"name": "Lisa", "age": 20, "interests": ["C++", "Python", "Piano"]})
people.insert_one({"name": "Mike", "age": 27})
people.insert_one({"name": "Lisa", "age": 26, "interests": ["C++", "Python", "Piano"]})
people.insert_one({"name": "John", "age": 78})

# get all documents
for person in people.find():
    print(person)

# filter documents
print([p for p in people.find({"_id": mike_id})])
print([p for p in people.find({"age": {"$lt": 25}})])

# count documents
print(people.count_documents({"name": "Lisa"}))

# update document
people.update_one({"_id": mike_id}, {"$set": {"age": 27}})
print([p for p in people.find({"age": {"$gt": 25}})])

# delete documents
people.delete_many({"age": {"$lt": 25}})
print()
for person in people.find():
    print(person)
    
# group by name and get the average age of each person
print()
pipeline = [
    {
        "$group": {
            "_id": "$name",
            "averageAge": {"$avg": "$age"}
        }
    },
    {
        "$sort": SON([("averageAge", -1), ("_id", -1)])
    }
]

results = people.aggregate(pipeline)
for res in results:
    print(res)
