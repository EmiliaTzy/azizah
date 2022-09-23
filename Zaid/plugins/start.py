from Zaid import Zaid, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
Hai! {}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ **Saya Adalah Bot Untuk Memutar Musik Di Grup**.
‣ **Saya Memiliki Banyak Fitur Dalam Bot Musik**
‣ **Bot Ini Berbasis Telethon. Dan Stabil Dari Banyak Bot Musik Lainnya**!
‣ **Saya dapat melakukan hal-hal lain seperti pin dll**.
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ **Klik Menu Bantuan 🔘 Untuk Informasi Selebihnya ℹ️**.
"""

@Zaid.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("➕ Tambahkan Saya Ke Grupmu", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👨‍💻 Sumber Kode", "https://github.com/")],
        [Button.url("🗣️ Support", f"https://t.me/{Config.SUPPORT}"), Button.url("📣 ᴜᴘᴅᴀᴛᴇꜱ", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("Bantuan Dan Perintah", data="help")]])
       return

    if event.is_group:
       await event.reply("**Hai!Saya Sudah Aktif ✅**")
       return



@Zaid.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ Tambahkan Saya Ke Grupmu", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👨‍💻 Sumber Kode", "https://github.com/")],
        [Button.url("🗣️ Support", f"https://t.me/{Config.SUPPORT}"), Button.url("📣 ᴜᴘᴅᴀᴛᴇꜱ", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("Bantuan Dan Perintah", data="help")]])
       return
