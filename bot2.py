# coding: utf-8
import discord
from discord.ext import commands
import os
import random

client = discord.Client()
ACCESS_TOKEN =os.environ["ACCESS_TOKEN"]


class Foods(commands.Cog, name='食べ物'):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        """なにか画像があれば出すよ"""
        if message.content == "らーめん":
            rnd = random.randint(1, 12)
            await message.channel.send(file=discord.File(f"./ramen/r{rnd}.jpg"))
        else:
            return


class JapaneseHelpCommand(commands.DefaultHelpCommand):
    def __init__(self):
        super().__init__()
        self.commands_heading = "コマンド:"
        self.no_category = "その他"
        self.command_attrs["help"] = "コマンド一覧と簡単な説明を表示"

    def get_ending_note(self):
        return f"各コマンドの説明: $help <コマンド名>\n"


bot = commands.Bot(command_prefix='$', help_command=JapaneseHelpCommand())
bot.add_cog(Foods(bot=bot))
# 取得したトークンを「ACCESS_TOKEN」の部分に記入
bot.run(ACCESS_TOKEN)