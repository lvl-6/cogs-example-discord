###############################################################################
# cogs-example
# ./__init__.py
#
# Author: John C <https://lvl-6.github.io>
# Created: 28/09/2020
#
# Description:
# An example of how to use cogs in a Discord.py bot.
#
###############################################################################

import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot as BotBase

version = '0.1' #Don't ask me about version numbering
bot_token = os.getenv('TESTBOT_TOKEN') #Change this to suit your project


###############################################################################
# Bot Initialisation
###############################################################################

# We will load only the cogs in this list - in this example, that's only
# ./cogs/hello.py
extensions = ['cogs.hello']

bot = BotBase(
    command_prefix = commands.when_mentioned,
    description = 'I provide an example of Discord Cogs in action.',
    owner_ids = 0,
    case_insensitive = True,
    )

# Program is running as main (i.e. not imported by another program)
if __name__ == '__main__':
    for extension in extensions:
        bot.load_extension(extension)
        print('Loaded extension: ' + extension)

@bot.event
async def on_connect():
    print('Bot has connected to Discord.')

@bot.event
async def on_disconnect():
    print('Bot has disconnected from Discord.')

@bot.event
async def on_ready():
    print('Bot is ONLINE and READY.')


###############################################################################
# Program Execution
###############################################################################

bot.run(bot_token)
