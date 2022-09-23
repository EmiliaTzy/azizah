from telethon import events, Button
from Zaid import Zaid, BOT_USERNAME
from Config import Config


btn =[
    [Button.inline("Admin", data="admin"), Button.inline("Play", data="play")],
    [Button.inline("Home", data="start")]]

HELP_TEXT = "Selamat Datang Untuk membantu Bagian Menu\n\nKlik Tombol!"


@Zaid.on(events.NewMessage(pattern="[!?/]help"))
async def help(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_group:
       await event.reply("Hubungi saya di PM untuk mendapatkan menu bantuan yang tersedia!", buttons=[
       [Button.url("Bantuan dan Perintah!", "t.me/{}?start=help".format(BOT_USERNAME))]])
       return

    await event.reply(HELP_TEXT, buttons=btn)

@Zaid.on(events.NewMessage(pattern="^/start help"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    await event.reply(HELP_TEXT, buttons=btn)

@Zaid.on(events.callbackquery.CallbackQuery(data="help"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    await event.edit(HELP_TEXT, buttons=btn)
