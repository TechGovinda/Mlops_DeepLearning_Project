import os
import requests
import zipfile
from cnnClassifier import logger
from dataclasses import dataclass
from cnnClassifier.entity.config_entity import DataIngestionConfig

# Setup logger (ensure this is done only once in your main module)


# ✅ Main Data Ingestion Class
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self) -> str:
        """
        Downloads a ZIP file from a URL and saves it locally.
        Returns:
            str: Path to the downloaded ZIP file.
        """
        url = self.config.source_URL
        rootdir = self.config.root_dir
        filename = self.config.local_data_file

        os.makedirs(rootdir, exist_ok=True)
        zip_file_path = os.path.join(rootdir, filename)

        logger.info(f"Starting download from {url}")
        response = requests.get(url)

        if response.status_code == 200:
            with open(zip_file_path, "wb") as f:
                f.write(response.content)
            logger.info(f"ZIP file saved at: {zip_file_path}")
            return zip_file_path
        else:
            logger.error(f"Download failed with status code: {response.status_code}")
            raise Exception(f"Download failed with status code: {response.status_code}")

    def extract_zip_file(self) -> bool:
        """
        Extracts the downloaded ZIP file into the specified directory.
        Returns:
            bool: True if extraction is successful, else False.
        """
        zip_file_path = os.path.join(self.config.root_dir, self.config.local_data_file)
        unzip_path = self.config.unzip_dir

        if not os.path.exists(zip_file_path):
            logger.error(f"ZIP file not found at: {zip_file_path}")
            return False

        try:
            os.makedirs(unzip_path, exist_ok=True)
            with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
                zip_ref.extractall(unzip_path)
            logger.info(f"ZIP file extracted to: {unzip_path}")
            return True
        except zipfile.BadZipFile:
            logger.error("The file is not a valid ZIP archive.")
            return False
