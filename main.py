import logging
from basic_edr import edr_agent
from email_monitoring import email_monitor
from vulnerability_checker import vulnerability_checker
from report import report_generator

# Configure logging
logging.basicConfig(filename='security_monitoring.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info('Starting Basic Security Monitoring System')
    
    try:
        # Run Basic EDR Agent
        edr_agent.run()
        logging.info('Basic EDR Agent completed successfully')
    except Exception as e:
        logging.error(f'Error running Basic EDR Agent: {e}')
    
    try:
        # Run Basic Email Monitor
        email_monitor.run()
        logging.info('Basic Email Monitor completed successfully')
    except Exception as e:
        logging.error(f'Error running Basic Email Monitor: {e}')
    
    try:
        # Run Basic Vulnerability Checker
        vulnerability_checker.run()
        logging.info('Basic Vulnerability Checker completed successfully')
    except Exception as e:
        logging.error(f'Error running Basic Vulnerability Checker: {e}')
    
    try:
        # Generate Basic Report
        report_generator.run()
        logging.info('Basic Report Generation completed successfully')
    except Exception as e:
        logging.error(f'Error generating Basic Report: {e}')

if __name__ == '__main__':
    main()
