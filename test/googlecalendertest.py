import datetime
import os.path
import pickle

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

