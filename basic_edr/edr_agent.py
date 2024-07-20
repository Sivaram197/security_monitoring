import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run():
    logging.info('Basic EDR Agent started')
    
    # Simplified logic for EDR agent
    suspicious_keywords = ['malware', 'attack', 'breach']
    log_file_path = 'sample_logs/system.log'
    
    try:
        with open(log_file_path, 'r') as file:
            logs = file.readlines()
        
        for log in logs:
            if any(keyword in log for keyword in suspicious_keywords):
                logging.warning(f'Suspicious activity detected: {log.strip()}')
                
    except FileNotFoundError:
        logging.error(f'Log file not found: {log_file_path}')
    
    logging.info('Basic EDR Agent completed')

# Creating a sample log file with some data
import os

sample_logs_dir = 'sample_logs'
os.makedirs(sample_logs_dir, exist_ok=True)

sample_log_data = """\
2023-07-18 10:00:00 - INFO - System boot
2023-07-18 10:05:00 - WARNING - Suspicious login attempt detected
2023-07-18 10:10:00 - INFO - User logged in
2023-07-18 10:15:00 - ERROR - Malware detected in file upload
2023-07-18 10:20:00 - INFO - System scan completed
2023-07-18 10:25:00 - INFO - System shutdown
"""

with open('sample_logs/system.log', 'w') as file:
    file.write(sample_log_data)

# Run the EDR agent
run()