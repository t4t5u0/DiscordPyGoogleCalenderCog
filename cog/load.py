from discord.ext import commands

from GoogleCalendarCog import GoogleCalendarCog

def setup(bot: commands.Bot):
    "cog を追加するやつ"
    return bot.add_cog(GoogleCalendarCog(bot))
