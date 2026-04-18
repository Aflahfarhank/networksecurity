from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.entity.config_entity import TrainingPipelineConfig, DataIngestionArtifact

import os
import sys
import numpy as np
import pandas as pd
import pymongo
from typing import List
from sklearn.model_selection import train_test_split

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)


class Dataingestion:
    def __init__(self, data_ingestion_config:TrainingPipelineConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e, sys)


    def export_collection_as_dataframe(self):
        """
        Export the collection data as a dataframe.
        """
        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            collection=self.mongo_client[database_name][collection_name]

            dataframe = pd.DataFrame(list(collection.find()))
            if "_id" in dataframe.columns.to_list():
                dataframe.drop("_id", axis=1, inplace=True)

            dataframe.replace(to_replace="na", value=np.NAN, inplace=True)
            return dataframe
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            dataframe = self.export_collection_as_dataframe()
        except Exception as e:
            raise NetworkSecurityException(e, sys)