from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from PIL import Image, ImageDraw, ImageFont

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1njdbmnp042pPbi5jqzCWzu2Ffr0wYOAtQKcJnSMvXwc'
SAMPLE_RANGE_NAME = '14!A1:E'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    AA = 'agree'
    r = [] #int
    a = [] #str
    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            r.append(int(row[0]))
            print(row[0])

    if AA == 'agree':
        r[0] = r[0] + 1
    if AA == 'oppose':
        r[1] = r[1] + 1    

    a.append(str(r[0]))
    a.append(str(r[1]))

    values = [
    [
        a[0]
    ],
    [
        a[1]
    ]
    # Additional rows ...
    ]
    body = {
    'values': values
    }
    result = service.spreadsheets().values().update(
    spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME,
    valueInputOption='RAW', body=body).execute()

if __name__ == '__main__':
    main()