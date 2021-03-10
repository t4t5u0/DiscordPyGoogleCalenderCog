import datetime
import os.path
import pickle

import discord
from discord.ext import commands
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


class GoogleCalendarCog(commands.Cog, name="googlecalender"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        # ログイン処理など
        # If modifying these scopes, delete the file token.pickle.
        self.SCOPES = ['https://www.googleapis.com/auth/calendar']
    

    @commands.Cog.listener()    
    async def on_start(self):
        return

    @commands.command()
    async def gcreg(self, ctx: commands.Context, link):
        """登録処理"""
        # URL -> id はスクレイピングするしかない？

    @commands.command()
    async def gcadd(self, ctx: commands.Context, *args):
        "現在のカレンダーに予定を追加する"
        return

    @commands.command()
    async def gcrm(self, ctx: commands.Context, *args):
        "予定を削除する"
        return

    @commands.command()
    async def gcls(self, ctx: commands.Context, *args):
        "予定一覧を表示する"
        return
    
    @commands.command(aliases=['calls'])
    async def gccalls(self, ctx: commands.Context, *args):
        "登録されているカレンダーの一覧を表示する"
        return

    @commands.command(aliases=['calrm'])
    async def gccalrm(self, ctx: commands.Context, *args):
        "登録されているカレンダーを削除する"
        return

    @commands.command(aliases=['chcal'])
    async def gcchcal(self, ctx: commands.Context, *args):
        "処理対象のカレンダーを変更する。"
        return

    @commands.command(aliases=['setch'])
    async def gcsetch(self, ctx: commands.Context, *args):
        "通知送信先チャンネルを設定する"


def setup(bot: commands.Bot):
    "cog を追加するやつ"
    return bot.add_cog(GoogleCalendarCog(bot))
