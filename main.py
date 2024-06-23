import logging
from basic_edr import edr_agent
from email_monitoring import email_monitor
from vulnerability_checker import vulnerability_checker
from report import report_generator

logging.basicConfig(filename='security_monitoring.log', level=logging.INFO)

def main():
    logging.info('Starting Basic Security Monitoring System')
    
    # Run Basic EDR Agent
    edr_agent.run()
    
    # Run Basic Email Monitor
    email_monitor.run()
    
    # Run Basic Vulnerability Checker
    vulnerability_checker.run()
    
    # Generate Basic Report
    report_generator.run()

if __name__ == '__main__':
    main()
