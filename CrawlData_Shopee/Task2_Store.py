import pandas as pd
from pymongo import MongoClient
from pymongo.server_api import ServerApi

class Task2_Local_Store:
    def __init__(self):
        # Connect to the MongoDB server
        self.client = MongoClient('mongodb://localhost:27017/')
        # Switch to the desired database
        self.db = self.client['Task2_Database']
        # Create a collection called 'employees'
        self.collection = self.db['shopee_data']
    
    def insert_data(self,df):
        dict_df = df.to_dict('records')
        result = self.collection.insert_many(dict_df)
        print ('=> Inserted document IDs successfuly:', result.inserted_ids)

class Task2_Remote_Store:
    def __init__(self):
        # Connect to the MongoDB server
        self.password = "hoangthinhnguyen"
        self.uri = "mongodb+srv://hoangthinhnguyen:{}@cluster0.1wsiirv.mongodb.net/?retryWrites=true&w=majority".format(self.password)

        # Create a new client and connect to the server
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))

        # Send a ping to confirm a successful connection
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
        
        # Switch to the desired database
        self.db = self.client['Task2_Database']
        
        # Create a collection called
        self.collection = self.db['shopee_data']
    
    def insert_data(self,df):
        dict_df = df.to_dict('records')
        result = self.collection.insert_many(dict_df)
        print ('=> Inserted document IDs successfuly:', result.inserted_ids)