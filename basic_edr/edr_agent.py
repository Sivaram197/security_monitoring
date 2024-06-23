import logging

def run():
    logging.info('Basic EDR Agent started')
    
    # Simplified logic for EDR agent
    # For example, checking a sample log file for suspicious activities
    suspicious_keywords = ['malware', 'attack', 'breach']
    log_file_path = 'sample_logs/system.log'
    
    with open(log_file_path, 'r') as file:
        logs = file.readlines()
    
    for log in logs:
        if any(keyword in log for keyword in suspicious_keywords):
            logging.warning(f'Suspicious activity detected: {log.strip()}')
    
    logging.info('Basic EDR Agent completed')
