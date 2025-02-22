import os
from pyrogram import Client






bot_token = os.environ.get("BOT_TOKEN")
api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
plugins = dict(root="plugins")

Bot = Client(
    "URL-Shortner-Bot",
    bot_token=bot_token,
    api_id=api_id,
    api_hash=api_hash,
    plugins=plugins,
    workers=50,
    sleep_threshold=10
)

Bot.run()
