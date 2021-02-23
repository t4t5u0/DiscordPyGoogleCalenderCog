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

CALENDAR_ID = "85th9cmqi2p3sf66kh60iqls6c@group.calendar.google.com"


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
    events_result = service.events().list(calendarId=CALENDAR_ID, timeMin=now,
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

    # page_token = None
    # while True:
    #     events = service.events().list(calendarId='85th9cmqi2p3sf66kh60iqls6c@group.calendar.google.com', pageToken=page_token).execute()
    #     for event in events['items']:
    #         pprint(event)
    #     page_token = events.get('nextPageToken')
    #     if not page_token:
    #         break

    event = {
        'summary': 'test post',
        'description': 'test',
        'start': {
            'dateTime': '2021-02-24T09:00:00',
            'timeZone': 'Asia/Tokyo',
        },
        'end': {
            'dateTime': '2021-02-24T10:00:00',
            'timeZone': 'Asia/Tokyo',
        },
    }
    # event = service.events().insert(calendarId=CALENDAR_ID, body=ex_text).execute()
    # event = {
    #     'summary': 'Google I/O 2015',
    #     'location': '800 Howard St., San Francisco, CA 94103',
    #     'description': 'A chance to hear more about Google\'s developer products.',
    #     'start': {
    #         'dateTime': '2015-05-28T09:00:00-07:00',
    #         'timeZone': 'America/Los_Angeles',
    #     },
    #     'end': {
    #         'dateTime': '2015-05-28T17:00:00-07:00',
    #         'timeZone': 'America/Los_Angeles',
    #     },
    #     'recurrence': [
    #         'RRULE:FREQ=DAILY;COUNT=2'
    #     ],
    #     'attendees': [
    #         {'email': 'lpage@example.com'},
    #         {'email': 'sbrin@example.com'},
    #     ],
    #     'reminders': {
    #         'useDefault': False,
    #         'overrides': [
    #             {'method': 'email', 'minutes': 24 * 60},
    #             {'method': 'popup', 'minutes': 10},
    #         ],
    #     },
    # }

    event = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))


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
