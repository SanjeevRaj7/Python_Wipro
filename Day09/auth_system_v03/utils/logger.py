import logging
from datetime import datetime

# Configure the logger
logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_request(endpoint, method, payload, status):
    logging.info(f"Endpoint: {endpoint}, Method: {method}, Payload: {payload}, Status: {status}")

def log_error(message):
    logging.error(f"Error: {message}")
