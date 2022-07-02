import os

credential_gmail_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'creds_gmail.json')
credential_sheets_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'creds_sheets.json')
SCOPES_DRIVE = ['https://www.googleapis.com/auth/drive']
SCOPES_GMAIL = ['https://mail.google.com/']
SCOPES_SHEETS = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
spreadsheet_id = ''  # insert here your google spreadsheet id
token_gmail_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'gmail_token.json')
token_drive_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'drive_token.json')
