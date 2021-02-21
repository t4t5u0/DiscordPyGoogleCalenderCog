import datetime
import os.path
import pickle

import discord
from discord.ext import commands
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


class GoogleCalenderCog(commands.Cog, name="googlecalender"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        # If modifying these scopes, delete the file token.pickle.
        SCOPES = ['https://www.googleapis.com/auth/calendar']
    

    @commands.Cog.listener()    
    async def on_start(self):
        return

    @commands.command()
    async def register(self, ctx: commands.Context, link):
        """hoge"""

    @commands.command()
    async def gcadd(self, ctx: commands.Context, *args):
        return