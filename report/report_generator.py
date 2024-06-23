import logging
import pandas as pd

def run():
    logging.info('Generating Basic Security Report')
    
    # Simplified logic for generating reports
    logs = []
    log_file_path = 'security_monitoring.log'
    
    with open(log_file_path, 'r') as file:
        for line in file:
            logs.append(line.strip())
    
    report_df = pd.DataFrame(logs, columns=['Log'])
    report_df.to_csv('report/security_report.csv', index=False)
    
    logging.info('Basic Security Report Generation completed')
