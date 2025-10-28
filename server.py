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

from fastapi import FastAPI
import time
import math
import logging
import uvicorn
import os

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Get default iterations from environment variable if set
DEFAULT_ITERATIONS = int(os.getenv("PROCESS_ITERATIONS", 100_000_000))

app = FastAPI(
    title="CPU Load Simulator API",
    description="A FastAPI app to simulate heavy CPU load for educational purposes.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    """Health check endpoint"""
    logger.info("Health check request received.")
    return {"message": "CPU Load Simulator API is running."}

@app.get("/process")
def simulate_load(iterations: int = DEFAULT_ITERATIONS):
    """
    Simulate heavy CPU load by performing complex calculations.
    :param iterations: number of loop iterations to simulate CPU usage
    """
    logger.info(f"Processing request with {iterations:,} iterations.")
    start_time = time.time()

    result = 0
    for i in range(iterations):
        # heavier calculation for longer CPU load
        result += math.sqrt(i % 1000) * math.sin(i % 100) + math.log1p((i % 500) + 1)

    elapsed = time.time() - start_time
    logger.info(f"Completed processing {iterations:,} iterations in {elapsed:.3f} seconds.")

    return {
        "iterations": iterations,
        "result_sample": result,
        "execution_time_seconds": round(elapsed, 3)
    }

if __name__ == "__main__":
    logger.info("Starting FastAPI CPU Load Simulator server...")
    uvicorn.run(app, host="0.0.0.0", port=80)
