# This file is a part of TG-Direct-Link-Generator
from main.vars import Var
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Language(object):
    class en(object):
        START_TEXT = """
**Hola... Envíame cualquier archivo para obtener el enlace de descarga directa{}**\n
<i>Que disfrutes del bot creado con ❤️❤️ por @EL_Wizard</i>\n
<b><u>Comandos</u></b>\n
<b>➽ /help para obtener ayuda del bot</b>\n
<b>➽ /about para obtener información del bot</b>"""

        HELP_TEXT = """🔰 **Como Usar el bot?**

<b>➽ Envia o reenvia cualquier archivo de Telegram y te dare un enlace de descarga directa</b>\n
<b>➽ Si envia un archivo multimedia recibirá 2 enlaces uno para descargar y otro para ver</b>\n
<b>➽ La velocidad de descarga es superior a <u>6mb/s</u></b>

**<b><u>La duración del enlace son 24 horas**</b></u>

<b><u>Regla 🚸</u></b>
<b>La unica regla que voy a poner es que no me escriban por Privado para pedirme el código.</b></b>\n
Alguna duda o sugerencia contáctame</i> <b>: <a href='https://t.me/EL_Wizard'>*•.¸♡𝓽​ꫝ​ꫀ​᭙𝓲ɀ​ꪖ𝘳​ᦔ•✖‿✖ ඞ</a></b>"""

        ABOUT_TEXT = """
<b>⚜ My Name:</b> ➳ᴹᴿ᭄ԲɿՆ૯੮૦ՆɿՈқ✤\n
<b>⚜ Username:</b> @file_to_link_Wizard_bot\n
<b>🔸Version:</b> 3.0\n
<b>🔹Última Actualización:</b> [ 29-Jun-22 ]
"""

        stream_msg_text ="""
<u>**Links Generado con Éxito 🙂🍧**</u>\n
<b>ඞ Nombre del archivo:</b> {}\n
<b>ඞ Tamaño del archivo:</b> {}\n
<b>ඞ Descargar:</b> {}\n
<b>ඞ Ver:</b> {}"""

        ban_text="__Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ.__\n\n**[Cᴏɴᴛᴀᴄᴛ Dᴇᴠᴇʟᴏᴘᴇʀ](https://t.me/EL_Wizard) Tʜᴇʏ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**"

# ------------------------------------------------------------------------------

class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Ayuda', callback_data='help'),
        InlineKeyboardButton('Información', callback_data='about')
        ],        
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Ayuda', callback_data='home'),
        InlineKeyboardButton('Información', callback_data='about')
        ],
        [
        InlineKeyboardButton('Atras', callback_data='close'),
        ],        
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Información', callback_data='home'),
        InlineKeyboardButton('Ayuda', callback_data='help')
        ],
        [
        InlineKeyboardButton('Atras', callback_data='close'),
        ]        
        ]
    )
