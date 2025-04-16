import logging as log
import os
from datetime import datetime

# Generate log filename with timestamp
LOG_FILE = f"{datetime.now().strftime('%m-%d-%Y-%H-%M-%S')}.log"

# Define logs directory
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Full path to the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Set up logging configuration
log.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=log.INFO,
)