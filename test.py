import urllib.parse
from pymongo import MongoClient

client = MongoClient("mongodb+srv://Kohelet:" + urllib.parse.quote("Ss1234!@") +
                     "@cluster0.upwxlcs.mongodb.net/?retryWrites=true&w=majority")
db = client.college
collection = db["students"]

result = collection.find_one({"name": {"$regex": "D"}})
print(result)
