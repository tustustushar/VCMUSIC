from pyrogram import Client as Bot

from callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN, BOT_USERNAME


bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    bot_username=BOT_USERNAME
    plugins=dict(root="handlers"),
)

bot.start()
run()
