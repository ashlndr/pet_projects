import httplib2

from setup import check_and_setup_modules

while True:
    try:
        from googleapiclient.discovery import build
        from oauth2client.service_account import ServiceAccountCredentials
        break
    except ImportError:
        check_and_setup_modules()

from credentials.credentials import credential_sheets_file, SCOPES_SHEETS, spreadsheet_id
from print_input_data import input_quarter, input_due_date, input_team_name


class GoogleSheet:
    """Class contains methods to obtain data from spreadsheet."""

    @staticmethod
    def get_all_sheet_data():
        """Get all spreadsheet data."""
        credentials = ServiceAccountCredentials.from_json_keyfile_name(credential_sheets_file, SCOPES_SHEETS)
        http_auth = credentials.authorize(httplib2.Http())
        service = build('sheets', 'v4', http=http_auth)
        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range=team_name,
            majorDimension='COLUMNS'
        ).execute()
        data = result.get("values")
        return data

    @staticmethod
    def return_list_of_names():
        """Get list of participants to evaluate."""
        list_of_names = []
        dict_output = {item[0]: item[1:] for item in all_sheet_data}
        for i in range(0, len(dict_output), 2):
            name = list(dict_output)[i]
            list_of_names.append(name)
        return list_of_names

    def return_list_of_mails(self):
        """Get list of corresponding mails."""
        list_of_mails = []
        dict_output = {item[0]: item[1:] for item in all_sheet_data}
        for name in self.return_list_of_names():
            for person in dict_output.keys():
                if name == person:
                    list_of_mails.append(dict_output.get(name))
        return list_of_mails

    @staticmethod
    def return_list_of_form_types():
        """Get list of google forms for corresponding mails."""
        list_of_form_types = []
        dict_output = {item[0]: item[1:] for item in all_sheet_data}
        for i in range(1, len(dict_output), 2):
            form = list(dict_output)[i]
            for form_type in dict_output.keys():
                if form == form_type:
                    list_of_form_types.append(dict_output.get(form))
        return list_of_form_types


team_name = input_team_name()
all_sheet_data = GoogleSheet.get_all_sheet_data()
names = GoogleSheet().return_list_of_names()
mails = GoogleSheet().return_list_of_mails()
form_types = GoogleSheet().return_list_of_form_types()
quarter = input_quarter()
due_date = input_due_date()
