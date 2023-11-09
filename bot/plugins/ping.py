from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot.client import Client
from pyrogram import filters
from pyrogram import types
from bot.core.db.add import add_user_to_database


@Client.on_message(filters.command(["start", "ping"]) & filters.private & ~filters.edited)
async def ping_handler(c: Client, m: "types.Message"):
    await add_user_to_database(c, m)
    await m.reply_photo(
       photo="https://graph.org/file/cb120e0ef770039b6881e.jpg",
       caption=f"""𝐇𝐞𝐥𝐥𝐨 𝐌𝐚𝐰𝐚 👋🏻 {m.from_user.mention} \n𝐈'𝐦 𝐀 𝐒𝐢𝐦𝐩𝐥𝐞 𝐅𝐢𝐥𝐞 𝐑𝐞𝐧𝐚𝐦𝐞 + 𝐅𝐢𝐥𝐞 𝐓𝐨 𝐕𝐢𝐝𝐞𝐨 𝐂𝐨𝐧𝐯𝐞𝐫𝐭𝐞𝐫 𝐁𝐎𝐓 𝐖𝐢𝐭𝐡 𝐏𝐞𝐫𝐦𝐚𝐧𝐞𝐧𝐭 𝐓𝐡𝐮𝐦𝐛𝐧𝐚𝐢𝐥 𝐒𝐮𝐩𝐩𝐨𝐫𝐭! 😎 \n𝐁𝐎𝐓 𝐂𝐑𝐄𝐀𝐓𝐄𝐃 𝐁𝐘 : <a href=https://t.me/Sunrises24BotUpdates>𝐒𝐔𝐍𝐑𝐈𝐒𝐄𝐒™</a> \n 🤩""",
       reply_markup=InlineKeyboardMarkup( [[
          InlineKeyboardButton("𝐎𝐖𝐍𝐄𝐑 🧑🏻‍💻", url='https://t.me/Sunrises_24')
          ],[
          InlineKeyboardButton('𝐂𝐇𝐀𝐍𝐍𝐄𝐋 🎞️', url='https://t.me/sunriseseditsoffical6'),
          InlineKeyboardButton('𝐔𝐏𝐃𝐀𝐓𝐄𝐒 📢', url='https://t.me/Sunrises24BotUpdates')
          ],[
          InlineKeyboardButton('𝐒𝐄𝐓𝐓𝐈𝐍𝐆𝐒 ⚙️', callback_data='showSettings')
          ]]
          )
       )
    


@Client.on_message(filters.command("help") & filters.private & ~filters.edited)
async def help_handler(c: Client, m: "types.Message"):
    if not m.from_user:
        return await m.reply_text("I don't know about you sar :(")
    await add_user_to_database(c, m)
    await c.send_flooded_message(
        chat_id=m.chat.id,
        text="I can rename media without downloading it!\n"
             "Speed depends on your media DC.\n\n"
             "Just send me media and reply to it with /rename command.\n\n"
             "To set custom thumbnail reply to any image with /set_thumbnail\n\n"
             "To see custom thumbnail press /show_thumbnail",
        reply_markup=types.InlineKeyboardMarkup([[
           types.InlineKeyboardButton("Show Settings",
                                      callback_data="showSettings")]])
    )
