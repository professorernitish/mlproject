# import logging
# import os
# from datetime import datetime

# LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d')}.log"
# logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
# os.makedirs(os.path,exist_ok=True)


# LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)


# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="%(asctime)s:%(levelname)s:%(message)s",
#     level=logging.INFO
# )



# if __name__ == "__main__":
#     logging.info("Logging has started") 



import logging
import os
from datetime import datetime

# Define log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d')}.log"

# Define logs directory path
logs_path = os.path.join(os.getcwd(), "logs")

# Create logs directory if it doesn't exist
os.makedirs(logs_path, exist_ok=True)

# Define full log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="%(asctime)s:%(levelname)s:%(message)s",
    level=logging.INFO
)

if __name__ == "__main__":
    logging.info("Logging has started")
        