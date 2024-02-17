import pymongo
from pymongo import MongoClient
import time

if __name__ == "__main__":
    print("Welcome to pymongo")
    client = pymongo.MongoClient()
    print(client)


    insert_multiple = [
        {
            'Name': 'Harry',
            'Age': 15,
            'House': 'Griffindore'

        },
        {
            'Name': 'Hermoine',
            'Age':15,
            'House':'Griffindore'
        },
        {
            'Name': 'Ron',
            'Age':15,
            'House':'Griffindore'
        }
    ]

    db = client["Hogwarts"]

    collections = db["Year-1"]

    collections.insert_many(insert_multiple)
    time.sleep(1)
    
