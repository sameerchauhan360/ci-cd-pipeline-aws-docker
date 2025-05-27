import sys
import os
from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.constants import DATABASE_NAME, MONGODB_URL_KEY
import pymongo
import certifi

ca = certifi.where()


class MongoDBClient:
    """
    Class Name: export data into feature store
    Description: This method export the dataframe from mongodb feature store as dataframe

    Output: Connection to mongodb database
    On Failure: raises and exception
    """

    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = MONGODB_URL_KEY
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {mongo_db_url} is not set.")

                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection succesfull")

        except Exception as e:
            raise USvisaException(e, sys)


if __name__ == "__main__":
    obj = MongoDBClient()
