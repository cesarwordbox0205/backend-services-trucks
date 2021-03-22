import logging
import urllib.request as request
import pandas as pd
import hashlib
import os
from dotenv import load_dotenv

DATASET_URL = "http://data.sfgov.org/resource/rqzj-sfat.csv"

REQUIRED_FEATURES = ["objectid", "applicant", "cnn"]
STRING_FEATURES = ["facilitytype", "locationdescription", "address", "blocklot", 
                    "block", "lot", "permit", "status", "fooditems", "schedule", 
                    "dayshours", "noisent", "approved", "expirationdate", "location"]
INTEGER_FEATURES = ["received", "priorpermit"]
FLOAT_FEATURES = ["x", "y", "latitude", "longitude", ":@computed_region_yftq_j783", ":@computed_region_p5aj_wyqh", ":@computed_region_rxqg_mtj9", ":@computed_region_bh8s_q3mv", ":@computed_region_fyvs_ahh9"]

DATAFILE_NAME = "stats.csv"

class FetchService():

    def __init__(self, truck_repository):
        self.truck_repository = truck_repository
        self.last_hash = None

    def process_data(self):
        logging.info("Fetching job started...")
        self._fetch_data()
        data_hash = get_hash(DATAFILE_NAME)
        last_hash = self._get_last_hash()
        if(last_hash is None or data_hash != last_hash):
            logging.info("Data changed since the last fetch operation...")
            logging.info("Last data hash {} Current data hash {}".format(last_hash, data_hash))
            data, is_valid = self._process_data(DATAFILE_NAME)
            if not is_valid:
                logging.info("Data has missing values in required features {}. Aborting operation...".format(REQUIRED_FEATURES))
            else:
                self._save_data(data)
                self._save_last_hash(data_hash)
        else:
            logging.info("Data has not changed since the last fetch operation...")
        logging.info("Operation completed...")

    def _fetch_data(self):
        logging.info("Fetching dataset from url {}".format(DATASET_URL))
        request.urlretrieve(DATASET_URL, DATAFILE_NAME)

    def _process_data(self, file):
        logging.info("Processing data...")
        data = pd.read_csv(file)
        return clean(data)

    def _save_data(self, data):
        logging.info("Saving data...")
        #data.apply(lambda x: self.truck_repository.save_record(x), axis = 1)
        total_records = len(data)
        for i, record in data.iterrows():
            self.truck_repository.save_record(record)
            if(i % 50 == 0):
                logging.info("Saved {}/{} records".format(i, total_records))

    def _get_last_hash(self):
        return self.truck_repository.get_last_hash()

    def _save_last_hash(self, hash):
        self.truck_repository.save_last_hash(hash)


def clean(data):
    if(data[REQUIRED_FEATURES].isnull().any().any()):
        return data, False
    data[STRING_FEATURES] = data[STRING_FEATURES].fillna("N/A")
    data[FLOAT_FEATURES] = data[FLOAT_FEATURES].fillna(data[FLOAT_FEATURES].mean())
    data[INTEGER_FEATURES] = data[INTEGER_FEATURES].fillna(data[INTEGER_FEATURES].mode())
    return data, True
    
    
def get_hash(file):
    BUF_SIZE = 32768 # Read file in 32kb chunks
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    with open(file, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
        sha1.update(data)
    return md5.hexdigest()





