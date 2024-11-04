# disk_monitor.py

import psutil
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='disk_usage.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Set disk usage threshold (in percentage)
DISK_USAGE_THRESHOLD = 80  # Warning threshold set at 80%

def check_disk_usage():
    """Check and log disk usage, alerting if usage exceeds the threshold."""
    # Get disk usage statistics
    disk_usage = psutil.disk_usage('/')

    # Log the current disk usage
    logging.info(f"Disk usage: {disk_usage.percent}%")
    
    # Check if disk usage exceeds threshold
    if disk_usage.percent > DISK_USAGE_THRESHOLD:
        logging.warning("Warning: Disk usage exceeds threshold!")
        print("Warning: Disk usage exceeds threshold!")
    else:
        print("Disk usage is within safe limits.")

# Run the disk usage check
if __name__ == "__main__":
    check_disk_usage()
