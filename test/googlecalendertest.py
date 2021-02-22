import datetime
import os.path
import pickle
from pprint import pprint

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# 実装して確認するもの
# 登録をコマンドライン上でする方法
# カレンダーを登録する
# タスクを登録する
# タスクを確認する
# タスクを削除する
# カレンダーを複数登録する

# 確認すること
# カレンダーごとにAuthをする必要があるのかどうか


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId="85th9cmqi2p3sf66kh60iqls6c@group.calendar.google.com", timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    # events_result = service.events().list(calendarId='primary', timeMin=now,
    #                                       maxResults=10, singleEvents=True,
    #                                       orderBy='startTime').execute()
    _events = events_result.get('items', [])

    if not _events:
        print('No upcoming events found.')
    for event in _events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

    page_token = None
    while True:
        events = service.events().list(calendarId='85th9cmqi2p3sf66kh60iqls6c@group.calendar.google.com', pageToken=page_token).execute()
        for event in events['items']:
            pprint(event)
        page_token = events.get('nextPageToken')
        if not page_token:
            break

if __name__ == '__main__':
    main()


# {
#    "kind": "calendar#calendarListEntry",
#    "etag": "\"1614023106785000\"",
#    "id": "85th9cmqi2p3sf66kh60iqls6c@group.calendar.google.com",
#    "summary": "test",
#    "description": "GoogleCalendarDiscordBot 用",
#    "timeZone": "Asia/Tokyo",
#    "colorId": "19",
#    "backgroundColor": "#c2c2c2",
#    "foregroundColor": "#000000",
#    "selected": true,
#    "accessRole": "owner",
#    "defaultReminders": [],
#    "conferenceProperties": {
#     "allowedConferenceSolutionTypes": [
#      "hangoutsMeet"
#     ]
#    }
# }