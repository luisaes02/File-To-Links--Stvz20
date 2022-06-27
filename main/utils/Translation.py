# This file is a part of TG-Direct-Link-Generator
from main.vars import Var
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Language(object):
    class en(object):
        START_TEXT = """
**👋 Hola. Bienvenid@ {}**\n
<i>Soy un bot para Generar links de Descarga Directa</i>\n
<b><i><u>Cuidado 🚸</u></i></b>\n
<b>🔞 Evite enviar contenido pornográfico al bot o será baneado permanentemente del bot.</b>"""

        HELP_TEXT = """🔰 **Como Usarme ?**

<i>- Send Me Any File Or Media From Telegram.</i>
<i>- I Will Provide External Direct Download Link !</i>

**Download Link With Fastest Speed ⚡️**

<b><i><u>Warning 🚸</u></i></b>
<b>🔞 Evite enviar contenido pornográfico al bot o será baneado permanentemente del bot.</b></b>\n
Contactar con mi Desarrallador para reportar Bug</i> <b>: <a href='https://t.me/LAES2002'>[ Contactar ]</a></b>"""

        ABOUT_TEXT = """
<b>⚜ My Name : File To Links Pro Generator</b>\n
<b>⚜ Username : @FileToLinksPro_bot</b>\n
<b>🔸Version : 2.0</b>\n
<b>🔹Last Updated : [ 04-Apr-22 ]</b>
"""

        stream_msg_text ="""
<u>**Links Generado con Éxito  !**</u>\n
<b>📂 File Name :</b> {}\n
<b>📦 File Size :</b> {}\n
<b>📥 Download :</b> {}\n
<b>🖥 Watch :</b> {}"""

        ban_text="__Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ.__\n\n**[Cᴏɴᴛᴀᴄᴛ Dᴇᴠᴇʟᴏᴘᴇʀ](https://t.me/TechZBots_Support) Tʜᴇʏ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**"

# ------------------------------------------------------------------------------

class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('About', callback_data='about')
        ],        
        [InlineKeyboardButton("Updates Channel", url='https://t.me/TechZBots'),
        InlineKeyboardButton("Repo", url='https://github.com/TechShreyash/TG-Direct-Link-Generator')]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('About', callback_data='about')
        ],
        [
        InlineKeyboardButton('Close', callback_data='close'),
        ],        
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Help', callback_data='help')
        ],
        [
        InlineKeyboardButton('Close', callback_data='close'),
        ]        
        ]
    )
