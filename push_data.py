import os
import sys
import json

from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca = certifi.where() #ca = certifi.where() is used to get the path to the certificate authority (CA) bundle.

import pandas as pd 
import numpy as np 
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging


class networkDataextract:

    def __init__(self):
        try:
            pass
        except Exception as e: 
            raise NetworkSecurityException(e, sys)
        
    def cv_to_json(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(inplace=True, drop=True)
            records = list(json.loads(data.T.to_json()).values())
            return records

        except Exception as e: 
            raise NetworkSecurityException(e, sys)
        
    def push_data_to_mongo(self, records, database, collection):
        try: 
            self.database=database,
            self.collection=collection,
            self.records=records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]

            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == "__main__":
    FILEPATH="Network_data\phising_data.csv"
    DATABASE = " "
    collection = "Network_data"
    networkobj = networkDataextract()
    records = networkobj.cv_to_json(FILEPATH)
    print(records[0])
    no_of_records = networkobj.push_data_to_mongo(records, DATABASE, collection)
    print(f"Number of records inserted to MongoDB: {no_of_records}")