import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.fastboot(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    fboot = f"fastboot"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{fboot} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)
