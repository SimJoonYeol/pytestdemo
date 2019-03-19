# -*- coding: utf-8 -*-

import pymongo

def get_mongodb():
    client = pymongo.MongoClient('localhost', 27017)
    db = client.test_database
    return db.collection_names()
