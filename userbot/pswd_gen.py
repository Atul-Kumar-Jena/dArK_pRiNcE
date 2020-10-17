import random
import string
from userbot.utils import admin_cmd
from telethon import event, errors, functions, types
import asyncio


@borg.on(admin_cmd(pattern=r"pswrd(?: |$)(.*)"))
async def get_random_string(event):
    if event.fwd from:
        return
    await event.edit("Processing your pswd...")
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id

    letters = string.ascii_letters
    result_stt = ''.join(random.choice(letters) for i in range(event))
    await.event.edit(Your Password is:), result_str
get_random_string(8)
get_random_string(8)
