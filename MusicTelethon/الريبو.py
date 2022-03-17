import os
import sys
from datetime import datetime
from time import time
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HNDLR, SUDO_USERS
START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (    ("Minggu", 60 * 60 * 24 * 7),    ("Hari", 60 * 60 * 24),    ("Jam", 60 * 60),    ("Menit", 60),    ("Detik", 1),)
async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(    filters.user(SUDO_USERS) & filters.command(["ريستارت"], prefixes=f"{HNDLR}"))
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("1")
    await loli.edit("2")
    await loli.edit("3")
    await loli.edit("4")
    await loli.edit("5")
    await loli.edit("6")
    await loli.edit("7")
    await loli.edit("8")
    await loli.edit("9")
    await loli.edit("**✅ تم إعادة تشتغل")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
@Client.on_message(filters.command(["الاوامر"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HELP = f"""
<b>👋 اهلا {m.from_user.mention}!

𝘰𝘳𝘥𝘦𝘳𝘴 𝘮𝘶𝘴𝘪𝘤 [ 𝘫𝘦𝘱𝘵𝘩𝘰𝘯 ](t.me/lMl10l)
——————×—————

⧉ | لتشغيل صوتية في المكالمة أرسل ⇦ [ `{HNDLR}تش  + اسم الاغنية` ]
⧉ | لتشغيل فيديو في المكالمة  ⇦ [ `{HNDLR}تشف  + اسم الاغنية` ]
———————×———————

⧉ | لأيقاف الاغنية او الفيديو مؤقتآ  ⇦ [ `{HNDLR}اف` ] 
⧉ | لأعاده تشغيل الاغنية ⇦  [ `{HNDLR}ايف` ]
⧉ | لأيقاف الاغنية  ⇦ [ `{HNDLR} ايق` ] 
⧉ | لتغطي الاغنية الحالية و تشغيل الاغنية التالية ⇦ [ `{HNDLR}التالي` ]
⧉ | لتشغيل الاغنية عشوائية من قناة او مجموعة  ⇦ [ `{HNDLR}اغنية` ]
———————×———————

⧉ | لتحميل صوتية أرسل ⇦ [ `{HNDLR}تح + اسم الاغنية او الرابط` ]
⧉ | لتحميل فيديو  ⇦  [ `{HNDLR}تحف + اسم الاغنية او الرابط` ]
———————×———————

⧉ | لأعاده تشغيل التنصيب أرسل ⇦  [ `{HNDLR}ريستارت` ]
———————×———————
🛠 """
    await m.reply(HELP)
@Client.on_message(filters.command(["الريبو"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>👋  اهلا {m.from_user.mention}!

🎶 المطور  @VOO0V
اخو المطور @Tgjggtm

"""
    await m.reply(REPO, disable_web_page_preview=True)
