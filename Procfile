import uuid
import logging

from pyrogram import Client, filters, StopPropagation
from pyrogram.types import Message
from telegraph import upload_file

from Devil.utils import get_user_tmp, cleanup_user_tmp, SHARE_BUTTON, SUCCESS_TEXT, ERROR_TEXT

logger = logging.getLogger(__name__)


@Client.on_message(filters.photo)
async def handle_photo(client: Client, message: Message):
    """Handle images sent as compressed photos (JPG/JPEG/PNG)."""
    chat_id = message.chat.id
    tmp = get_user_tmp(chat_id)
    file_path = f"{tmp}/{uuid.uuid4()}.jpg"

    status = await message.reply_text("📥 Downloading your image...")

    try:
        file_path = await client.download_media(message=message, file_name=file_path)
        await status.edit_text("📤 Uploading to Telegraph...")

        response = upload_file(file_path)
        tg_url = f"https://telegra.ph{response[0]}"

        await status.edit_text(
            SUCCESS_TEXT.format(url=tg_url),
            disable_web_page_preview=True,
            reply_markup=SHARE_BUTTON(tg_url),
        )

    except Exception as e:
        logger.error(f"Photo upload error: {e}")
        await status.edit_text(ERROR_TEXT.format(error=str(e)))

    finally:
        cleanup_user_tmp(chat_id)

    raise StopPropagation
