import asyncio
import importlib

# --- KURIGRAM BUTTON PATCH START ---
from kurigram.types import InlineKeyboardButton, ButtonStyle

original_button_init = InlineKeyboardButton.__init__

def custom_button_init(self, text, callback_data=None, style=None, **kwargs):
    if style is None:
        text_lower = text.lower()
        if "❌" in text or "close" in text_lower or "cancel" in text_lower or "back" in text_lower:
            style = ButtonStyle.DANGER
        elif "✅" in text or "add" in text_lower or "pay" in text_lower or "success" in text_lower:
            style = ButtonStyle.SUCCESS
        else:
            style = ButtonStyle.PRIMARY 
            
    original_button_init(self, text=text, callback_data=callback_data, style=style, **kwargs)

InlineKeyboardButton.__init__ = custom_button_init
# --- KURIGRAM BUTTON PATCH END ---

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from PRINCEMUSIC import LOGGER, app, userbot
from PRINCEMUSIC.core.call import PRINCE
from PRINCEMUSIC.misc import sudo
from PRINCEMUSIC.plugins import ALL_MODULES
from PRINCEMUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐢𝐥𝐥 𝐀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐒𝐞𝐬𝐬𝐢𝐨𝐧")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("PRINCEMUSIC.plugins" + all_module)
    LOGGER("PRINCEMUSIC.plugins").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")
    await userbot.start()
    await PRINCE.start()
    try:
        await PRINCE.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("PRINCEMUSIC").error(
            "𝗣𝗹𝗭 𝗦𝗧𝗔𝗥𝗧 𝗬𝗢𝗨𝗥 𝗟𝗢𝗚 𝗚𝗥𝗢𝗨𝗣 𝗩𝗢𝗜𝗖𝗘𝗖𝗛𝗔𝗧\𝗖𝗛𝗔𝗡𝗡𝗘𝗟\n\n𝗣𝗥𝗜𝗡𝗖𝗘 𝗕𝗢𝗧 𝗦𝗧𝗢𝗣........"
        )
        exit()
    except:
        pass
    await PRINCE.decorators()
    LOGGER("PRINCEMUSIC").info(
        "╔═════ஜ۩۞۩ஜ════╗\n  ☠𝗠𝗔𝗗𝗘 𝗕𝗬 𝗠𝗥 𝗣𝗥𝗜𝗡𝗖𝗘\n╚═════ஜ۩۞۩ஜ════╝"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("PRINCEMUSIC").info("𝗦𝗧𝗢𝗣 𝗣𝗥𝗜𝗡𝗖𝗘 𝗠𝗨𝗦𝗜𝗖🎻 𝗕𝗢𝗧..")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
