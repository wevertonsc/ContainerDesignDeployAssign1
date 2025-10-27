"""
This is an academic project for the Master's program at TUS Midlands. For educational purposes and academic collaboration.
License: Academic Project - TUS Midlands 2025
Student Information:
Name: Weverton de Souza Castanho
Program: Master of Science in Software Design with Cloud Native Computing
Course: Container Design and Deployment (AL_KCNCM_9_1) 29433
Institution: TUS - Technological University of the Shannon: Midlands Midwest
Year: 2025
"""

import requests
import time
import logging

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

SERVER_URL = "http://127.0.0.1:8000"

# Iteration levels for heavy load testing
ITERATION_LEVELS = [10_000_000, 50_000_000, 100_000_000]

def test_load(iterations: int):
    """Send a request to the server to simulate heavy CPU load"""
    url = f"{SERVER_URL}/process?iterations={iterations}"
    logger.info(f"Sending request to {url}")
    start = time.time()

    try:
        response = requests.get(url)
        elapsed = time.time() - start

        if response.status_code == 200:
            logger.info(f"Response: {response.json()}")
        else:
            logger.error(f"Error: {response.status_code} - {response.text}")

        logger.info(f"Total round-trip time: {elapsed:.3f} seconds\n")
    except requests.exceptions.RequestException as e:
        logger.error(f"Request failed: {e}")

if __name__ == "__main__":
    logger.info("Starting load simulation client...")
    for i in ITERATION_LEVELS:
        test_load(i)
