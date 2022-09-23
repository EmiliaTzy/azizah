from telethon import events, Button
from Zaid import Zaid
from Zaid.status import *
from Config import Config
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import ExportChatInviteRequest

@Zaid.on(events.callbackquery.CallbackQuery(data="admin"))
async def _(event):

    await event.edit(ADMIN_TEXT, buttons=[[Button.inline("« 𝑲𝒆𝒎𝒃𝒂𝒍𝒊", data="help")]])

@Zaid.on(events.callbackquery.CallbackQuery(data="play"))
async def _(event):

    await event.edit(PLAY_TEXT, buttons=[[Button.inline("« 𝑲𝒆𝒎𝒃𝒂𝒍𝒊", data="help")]])


ADMIN_TEXT = """
**✘ Modul yang dapat digunakan oleh admin obrolan!**
`?end` - Untuk Mengakhiri streaming musik.
`?skip` - Untuk Melewati Trek yang Sedang Berjalan.
`?pause` - Untuk Menjeda streaming.
`?resume` - untuk Melanjutkan Streaming.
`?leavevc` - memaksa Userbot keluar dari Vc Chat (Terkadang Bergabung).
`?playlist` - untuk memeriksa daftar putar.
"""

PLAY_TEXT = """
**✘ Modul yang dapat digunakan oleh pengguna obrolan!**
`?play` - Untuk Memutar Audio dari Yang Lain Balas ke file audio.
`?vplay` - Untuk Streaming Video (HEROKU_MODE > Tidak mendukung).
"""
