import os
import urllib.request as requests
import zipfile
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path



class DataIngestionConfig:
    def __init__(self, root_dir, source_URL, local_data_file, unzip_dir):
        self.root_dir = root_dir
        self.source_URL = source_URL
        self.local_data_file = local_data_file
        self.unzip_dir = unzip_dir



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, header = requests.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{header}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    
    def extract_zip_file(self):
        """
        zip_file_path = str
        Extract the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            


        