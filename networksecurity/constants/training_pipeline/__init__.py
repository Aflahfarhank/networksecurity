import os
import sys
import numpy as np 
import pandas as pd


"""
This is the __init__.py file for the training_pipeline module. It contains constants that are used throughout the training pipeline.
"""
TARGET_COLUMN = "label"
PIPELINE_NAME = "network_security"
ARTIFACT_DIR = "artifact"
FILE_NAME = "phishing_data.csv"

TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

"""
DATA ingestion related constants start with DATA_INGESTION VAR NAME

"""

DATA_INGESTION_COLLECTION_NAME = "Network_data"
DATA_INGESTION_DATABASE_NAME = "Network_security"
DATA_INGESTION_DIR_NAME = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR = "feature_store"
DATA_INGESTION_INGESTED_DIR = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2