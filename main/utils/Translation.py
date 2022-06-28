# This file is a part of TG-Direct-Link-Generator
from main.vars import Var
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Language(object):
    class en(object):
        START_TEXT = """
**Hola... Bienvenido al bot de @EL_Wizard {}**\n
<i>Bot creado para genarar descrgado directa</i>\n
<b><i><u>Cuidado</u></i></b>\n
<b>El que envie porno lo baneo 😑🍧</b>"""

        HELP_TEXT = """🔰 **Como Usarme ?**

<i>- Reenvíame un archivo de Telegram para Generar el enlace de Descarga Directa.</i>

**Download Link With Fastest Speed ⚡️**

<b><i><u>Warning 🚸</u></i></b>
<b>🔞 Evite enviar contenido pornográfico al bot o será baneado permanentemente del bot.</b></b>\n
Contactar con mi Desarrallador para reportar Bug</i> <b>: <a href='https://t.me/LAES2002'>[ Contactar ]</a></b>"""

        ABOUT_TEXT = """
<b>⚜ My Name : File To Links Pro Generator</b>\n
<b>⚜ Username : @file_to_link_Wizard_bot</b>\n
<b>🔸Version : 2.0</b>\n
<b>🔹Last Updated : [ 27-Jun-22 ]</b>
"""

        stream_msg_text ="""
<u>**Links Generado con Éxito  !**</u>\n
<b>ඞ File Name :</b> {}\n
<b>ඞ File Size :</b> {}\n
<b>ඞ Download :</b> {}\n
<b>ඞ Watch :</b> {}"""

        ban_text="__Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ.__\n\n**[Cᴏɴᴛᴀᴄᴛ Dᴇᴠᴇʟᴏᴘᴇʀ](https://t.me/EL_Wizard) Tʜᴇʏ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**"

# ------------------------------------------------------------------------------

class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Ayuda', callback_data='help'),
        InlineKeyboardButton('Info', callback_data='about')
        ],        
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Ayuda', callback_data='home'),
        InlineKeyboardButton('Info', callback_data='about')
        ],
        [
        InlineKeyboardButton('Close', callback_data='close'),
        ],        
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Infl', callback_data='home'),
        InlineKeyboardButton('Ayuda', callback_data='help')
        ],
        [
        InlineKeyboardButton('Close', callback_data='close'),
        ]        
        ]
    )
