from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_photo("https://telegra.ph/file/002151a1eb0040d0b7b90.jpg")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎀
ι ϲᴀɴ ρʟᴀʏ мᴜѕɪᴄ ιɴ γᴏᴜʀ gʀᴏᴜᴩ νᴏɪᴄᴇ ϲʜᴀᴛ. ∂ᴇᴠᴇʟᴏᴩᴇᴅ ϐʏ  [【TUSHAR】💞【ROMANTIC❤SHAYAR】](https://t.me/TUSHAR204) .
αᴅᴅ мᴇ τᴏ γᴏᴜʀ gʀᴏᴜᴩ αɴᴅ ρʟᴀʏ мᴜѕɪᴄ ƒʀᴇᴇʟʏ!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐎𝐖𝐍𝐄𝐑😘", url="t.me/tushar204")
                  ],[
                    InlineKeyboardButton(
                        "𝐒𝐔𝐏𝐏𝐎𝐑𝐓👿", url="https://t.me/LOVELYAPPEAL"
                    ),
                    InlineKeyboardButton(
                        "𝐂𝐇𝐀𝐍𝐍𝐄𝐋", url="https://t.me/ABOUTVEDMAT"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "𝐌𝐀𝐈𝐍 𝐑𝐎𝐁𝐎𝐓", url="https://t.me/LOVELYR_OBOT"
                    )
                ],[
                    InlineKeyboardButton(
                        "➕𝐀𝐃𝐃 𝐓𝐎 𝐆𝐑𝐎𝐔𝐏➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Aᴍ Oɴʟɪɴᴇ ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊𝐔𝐏𝐃𝐀𝐓𝐄𝐒", url="https://t.me/ABOUTVEDMAT")
                ]
            ]
        )
   )
