import os
import logging
from datetime import datetime

def error_log(message, log_level=logging.ERROR):
    # Step 1: Create a 'logs' folder if it doesn't exist
    logs_folder = 'logs'
    if not os.path.exists(logs_folder):
        os.makedirs(logs_folder)

    # Step 2: Configure Logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Create a file handler for errors with timestamp
    timestamp = datetime.now().strftime("%d%m%Y")
    log_file = os.path.join(logs_folder, f'LOGS_{timestamp}.txt')
    error_handler = logging.FileHandler(log_file)
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    # Add the error handler to the root logger
    logging.getLogger().addHandler(error_handler)

    # Use the specified log level
    if log_level == logging.DEBUG:
        logging.debug(message)
    elif log_level == logging.INFO:
        logging.info(message)
    elif log_level == logging.WARNING:
        logging.warning(message)
    elif log_level == logging.ERROR:
        logging.error(message)
    elif log_level == logging.CRITICAL:
        logging.critical(message)
    else:
        raise ValueError("Invalid log level")

    # Step 5: Handle Exceptions
    try:
        # Your code that might raise an exception
        raise ValueError("Exception. Status: 🟢 ")
        
    except ValueError as e:
        logging.error("An error occurred:🔴 %s", str(e), exc_info=True)




