from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")

# Space-separated Telegram user IDs allowed to control the bot (no default on purpose)
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
