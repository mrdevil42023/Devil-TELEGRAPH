import logging
import os
import shutil

from pyrogram import Client, idle
from auth import Vauth

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)

# Validate env vars before starting
Vauth.validate()

BOT_TOKEN = Vauth.BOT_TOKEN
API_ID = Vauth.API_ID
API_HASH = Vauth.API_HASH

PLUGINS = dict(root="Devil")

# Temp folder used for downloads
TEMP_DIR = "TEMP_FILES"


def cleanup_temp():
    """Remove the global temp directory on start/stop."""
    try:
        shutil.rmtree(TEMP_DIR)
        logger.info("Cleaned up temp folder.")
    except Exception:
        pass


app = Client(
    "DevilxTelegraph",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins=PLUGINS,
    workers=10,
)

if __name__ == "__main__":
    cleanup_temp()
    logger.info("Starting Devil X Telegraph Bot...")
    app.start()
    logger.info("Bot started successfully!")
    idle()
    app.stop()
    cleanup_temp()
    logger.info("Bot stopped.")
