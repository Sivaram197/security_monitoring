import logging
import json

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_rules(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from file: {file_path}")
        return None

def check_email(email, rules):
    for rule in rules:
        if rule['type'] == 'subject' and rule['value'] in email['subject']:
            logging.warning(f'Suspicious email detected: {email}')
        elif rule['type'] == 'body' and rule['value'] in email['body']:
            logging.warning(f'Suspicious email detected: {email}')

def run():
    logging.info('Basic Email Monitor started')
    
    rules_data = load_rules('email_monitoring/rules.json')
    if rules_data is None:
        logging.error('Failed to load rules. Exiting.')
        return

    emails = [
        {"subject": "Your account has been breached", "body": "Please click this link to secure your account"},
        {"subject": "Meeting reminder", "body": "Don't forget our meeting at 3 PM"},
    ]
    
    for email in emails:
        check_email(email, rules_data['rules'])
    
    logging.info('Basic Email Monitor completed')

if __name__ == "__main__":
    run()
