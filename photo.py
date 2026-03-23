import os
import shutil
import logging

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

logger = logging.getLogger(__name__)

TEMP_DIR = "TEMP_FILES"

SHARE_BUTTON = lambda url: InlineKeyboardMarkup([[
    InlineKeyboardButton(
        text="👓 Share 👓",
        url=f"https://telegram.me/share/url?url={url}",
    )
]])

SUCCESS_TEXT = """**✅ Upload Successful!**

**🔗 Link:** `{url}`

🖥 Bot by [MR DEVIL](http://t.me/mrdevil12)
"""

ERROR_TEXT = """**❌ Upload Failed**

`{error}`

Please retry or report to @devilbotsupport
"""


def get_user_tmp(chat_id: int) -> str:
    """Return a per-user temp directory path (created if missing)."""
    path = os.path.join(TEMP_DIR, str(chat_id))
    os.makedirs(path, exist_ok=True)
    return path


def cleanup_user_tmp(chat_id: int):
    """Remove only this user's temp folder."""
    path = os.path.join(TEMP_DIR, str(chat_id))
    try:
        shutil.rmtree(path)
    except Exception:
        pass
