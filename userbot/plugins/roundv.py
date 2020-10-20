import datetime

from telethon import events

from telethon.errors.rpcerrorlist import YouBlockedUserError

from telethon.tl.functions.account import UpdateNotifySettingsRequest

from userbot.utils import admin_cmd


#===================================================================================



@borg.on(admin_cmd("roundv ?(.*)"))

async def _(event):

    if event.fwd_from:

        return 

    if not event.reply_to_msg_id:

       await event.edit("```Reply to any users message.```")

       return

    reply_message = await event.get_reply_message() 

    if not reply_message.media:

       await event.edit("```reply to media message```")

       return

    chat = "@TelescopyBot"

    sender = reply_message.sender

    if reply_message.sender.bot:

       await event.edit("**Reply to actual users message.**")

       return

    await event.edit("**Processing weit..**")

    async with borg.conversation(chat) as conv:

          try:     

              response = conv.wait_event(events.NewMessage(incoming=True,from_users=397367589))

              await borg.forward_messages(chat, reply_message)

              response = await response 

          except YouBlockedUserError: 

              await event.reply("__Please unblock @TelescopyBot and try again__")

              return

              await event.delete()
              await event.client.send_message(event.chat_id, response.message)



