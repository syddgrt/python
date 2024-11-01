import psutil
import time
import datetime

def log_system_metrics():
    with open("system_metrics.log", "a") as log_file:
        while True:
            cpu_usage = psutil.cpu_percent()
            memory_info = psutil.virtual_memory()
            log_file.write(f"{datetime.datetime.now()}, CPU: {cpu_usage}%, Memory: {memory_info.percent}%\n")
            log_file.flush()  # Flush the buffer to ensure data is written
            time.sleep(60)  # Log every 60 seconds

if __name__ == "__main__":
    log_system_metrics()
