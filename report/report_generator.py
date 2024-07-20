import logging
import pandas as pd

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_logs(file_path):
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                logs.append(line.strip())
    except FileNotFoundError:
        logging.error(f"Log file not found: {file_path}")
        return None
    except Exception as e:
        logging.error(f"Error reading log file: {e}")
        return None
    return logs

def generate_report(logs, output_path):
    try:
        report_df = pd.DataFrame(logs, columns=['Log'])
        report_df.to_csv(output_path, index=False)
    except Exception as e:
        logging.error(f"Error writing report to CSV: {e}")
        return False
    return True

def run():
    logging.info('Generating Basic Security Report')
    
    log_file_path = 'security_monitoring.log'
    report_file_path = 'report/security_report.csv'
    
    logs = load_logs(log_file_path)
    if logs is None:
        logging.error('Failed to load logs. Exiting.')
        return
    
    if generate_report(logs, report_file_path):
        logging.info('Basic Security Report Generation completed')
    else:
        logging.error('Failed to generate security report')

if __name__ == "__main__":
    run()
