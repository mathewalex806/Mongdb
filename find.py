import pymongo
from pymongo import MongoClient
import time

if __name__ == "__main__":
    print("Welcome to pymongo")
    client = pymongo.MongoClient()


    db = client["Hogwarts"]

    collections = db["Year-1"]

    one = collections.find_one({'Name':'Hermoine'})
    print(one)
    time.sleep(1)
    
