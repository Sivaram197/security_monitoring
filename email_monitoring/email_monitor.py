import logging
import json

def run():
    logging.info('Basic Email Monitor started')
    
    with open('email_monitoring/rules.json', 'r') as f:
        rules = json.load(f)
    
    # Sample email data
    emails = [
        {"subject": "Your account has been breached", "body": "Please click this link to secure your account"},
        {"subject": "Meeting reminder", "body": "Don't forget our meeting at 3 PM"},
    ]
    
    for email in emails:
        for rule in rules['rules']:
            if rule['type'] == 'subject' and rule['value'] in email['subject']:
                logging.warning(f'Suspicious email detected: {email}')
            if rule['type'] == 'body' and rule['value'] in email['body']:
                logging.warning(f'Suspicious email detected: {email}')
    
    logging.info('Basic Email Monitor completed')
