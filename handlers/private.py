from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2

@Client.on_message(filters.command("noinoi") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**π‘πΌπΆπ»πΌπΆ π πππΆπ° ππΌπ π’π»πΉπΆπ»π² π‘πΌπ\nπ ππ»π·πΌπ π πππΆπ°<3**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "πΌπ’ππ»π²πΏ", url="https://t.me/BazigarYT")
                ]
            ]
        )
   )
