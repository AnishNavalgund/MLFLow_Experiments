import os
import shutil
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def import_from_sharepoint():
    source = os.getenv('SHAREPOINT_SOURCE_PATH')
    destination = os.getenv('LOCAL_DESTINATION_PATH')
    if source and destination:
        try:
            shutil.copytree(source, destination, dirs_exist_ok=True)
            logging.info("Successfully copied from Sharepoint")
        except Exception as e:
            logging.error(f"Error during copying from Sharepoint: {e}")
    else:
        logging.error("Source or destination path not set in environment variables")

def export_to_sharepoint():
    source = os.getenv('LOCAL_SOURCE_PATH')
    destination = os.getenv('SHAREPOINT_DESTINATION_PATH')
    if source and destination:
        try:
            shutil.copytree(source, destination, dirs_exist_ok=True)
            logging.info("Successfully copied to Sharepoint")
        except Exception as e:
            logging.error(f"Error during copying to Sharepoint: {e}")
    else:
        logging.error("Source or destination path not set in environment variables")