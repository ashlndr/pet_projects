from base64 import urlsafe_b64encode
from email.mime.text import MIMEText

from credentials.credentials import *
from google_auth import google_auth
from forms_links import forms_for_first_test, forms_for_second_test
from prepare_to_send import names, mails, form_types, quarter, due_date


def get_google_form_url_id():
    """Get google form id for evaluation type."""
    forms = (form for form_list in form_types for form in form_list)
    form_links = (forms_for_first_test.get(form) if form in forms_for_first_test.keys()
                  else forms_for_second_test.get(form) for form in forms)
    for form_link in form_links:
        url_id = form_link.split('/')[-2]
        return url_id


def form_mail(name=None, form_type=None, form_link=None, mail_to=None, mail_from=None):
    """Make message body."""
    msg = f'Hello! This is a test message about {name}. Due date to send is: {due_date}'
    subject = f'You have got the form to fill! {form_type}'
    message = f'{form_link}\n{msg}'
    message = MIMEText(message)
    message['subject'] = subject
    message['to'] = mail_to
    message['from'] = mail_from
    encoded_message = {'raw': urlsafe_b64encode(message.as_bytes()).decode()}
    return encoded_message


def send_google_forms():
    service_gmail = google_auth(scopes=SCOPES_GMAIL, token_path=token_gmail_file, service_name='gmail', version='v1',
                                creds_path=credential_gmail_file)
    service_drive = google_auth(scopes=SCOPES_DRIVE, token_path=token_drive_file, service_name='drive', version='v3',
                                creds_path=credential_gmail_file)
    mail_from = ''
    for name in names:
        print(f'{name}:')
        count = 0
        unique_form_type = []
        form_link_dict = {}
        for i in range(len(form_types)):
            for form_type, mail in zip(form_types[i], mails[i]):
                if form_type in [forms_for_first_test.keys(), forms_for_second_test.keys()]:
                    evaluation_form_type = form_type
                    mail_to = mail
                if count == 0 or evaluation_form_type not in unique_form_type:
                    origin_file_id = get_google_form_url_id()
                    copied_file_title = {'name': f'{name}. {form_type}. {quarter}'}
                    results = service_drive.files().copy(
                        fileId=origin_file_id, body=copied_file_title).execute()
                    form_id = results.get('id')
                    form_link = f'https://docs.google.com/forms/d/{form_id}/edit'
                elif unique_form_type[-1] != form_type:
                    form_link = form_link_dict.get(form_type)
                count += 1
                form_link_dict[form_type] = form_link
                unique_form_type.append(form_type)
                print(f'{mail_to}: {form_link}')
                message = form_mail(name, form_type, form_link, mail_to, mail_from)
                service_gmail.users().messages().send(userId=mail_from, body=message).execute()
                break
            form_types.pop(i)
            mails.pop(i)
            break
