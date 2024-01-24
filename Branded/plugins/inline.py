import asyncio

from .. import *
from .. import __version__
from ..modules.misc import *
from ..modules.utils import *
from pyrogram.types import *


async def help_menu_logo(answer):
    if var.USERBOT_PICTURE:
        thumb_image = var.USERBOT_PICTURE
    else:
        thumb_image = "https://telegra.ph/file/e8cd744688a8926d9afcb.jpg"
    button = paginate_plugins(0, PLUGINS, "help")
    answer.append(
        InlineQueryResultPhoto(
            photo_url=f"{thumb_image}",
            title="🥀 Help Menu ✨",
            thumb_url=f"{thumb_image}",
            description=f"🥀 Open Help Menu Of ❥❥𝙄 𝘼𝙢 𝙎𝙞𝙡𝙚𝙣𝙩࿐-Userbot ✨...",
            caption=f"""
**🥀 𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗧𝗢 𝗛𝗘𝗟𝗣 𝗠𝗘𝗡𝗨 𝗢𝗙
❥❥𝙄 𝘼𝙢 𝙎𝙞𝙡𝙚𝙣𝙩࿐ Userbot » {__version__} ✨...

𝗖𝗟𝗜𝗖𝗞 𝗢𝗡 𝗕𝗘𝗟𝗢𝗪 🌺 𝗕𝗨𝗧𝗧𝗢𝗡𝗦 𝗧𝗢
𝗚𝗘𝗧 𝗨𝗦𝗘𝗥𝗢𝗧 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦

🌷Powered By : [❥❥𝙄 𝘼𝙢 𝙎𝙞𝙡𝙚𝙣𝙩࿐](https://t.me/iamsilent1).**
            """,
            reply_markup=InlineKeyboardMarkup(button),
        )
    )
    return answer


async def help_menu_text(answer):
    button = paginate_plugins(0, PLUGINS, "help")
    answer.append(
        InlineQueryResultArticle(
            title="🥀 Help Menu ✨",
            input_message_content=InputTextMessageContent(f"""
**🥀 𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗧𝗢 𝗛𝗘𝗟𝗣 𝗠𝗘𝗡𝗨 𝗢𝗙
❥❥𝙄 𝘼𝙢 𝙎𝙞𝙡𝙚𝙣𝙩࿐ Userbot » {__version__} ✨...

𝗖𝗟𝗜𝗖𝗞 𝗢𝗡 𝗕𝗘𝗟𝗢𝗪 🌺 𝗕𝗨𝗧𝗧𝗢𝗡𝗦 𝗧𝗢
𝗚𝗘𝗧 𝗨𝗦𝗘𝗥𝗢𝗧 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦

🌷Powered By : [❥❥𝙄 𝘼𝙢 𝙎𝙞𝙡𝙚𝙣𝙩࿐](https://t.me/iamsilent1).**""",
            disable_web_page_preview=True
            ),
            reply_markup=InlineKeyboardMarkup(button),
        )
    )
    return answer


@bot.on_inline_query()
@inline_wrapper
async def inline_query_handler(bot, query):
    text = query.query
    if text.startswith("help_menu_logo"):
        answer = []
        answer = await help_menu_logo(answer)
        try:
            await bot.answer_inline_query(
                query.id, results=answer, cache_time=10
            )
        except Exception as e:
            print(str(e))
            return
    elif text.startswith("help_menu_text"):
        answer = []
        answer = await help_menu_text(answer)
        try:
            await bot.answer_inline_query(
                query.id, results=answer, cache_time=10
            )
        except Exception as e:
            print(str(e))
            return
    else:
        return
