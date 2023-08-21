import pymongo
from config import config

myclient = pymongo.MongoClient(config.mongoDbURL)
mydb = myclient["db"]
mycol = mydb["dt"]

def insert(keyword, l):
    x = mycol.insert_one({ "keyWord": keyword, "l": l })

def queryList(keyword):
    x=mycol.find_one({ "keyWord": keyword })
    return x["l"] if x else []

def getAllKeywords():
    return [i["keyWord"] for i in mycol.find({},{"keyWord": 1})]