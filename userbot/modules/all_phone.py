#created by @PM_The_Angry
#credit goes to @Vachounet for Permission
#thanks @Three_Cube_TeKnoways for Bug Fixing and Helping

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

@register(outgoing=True, pattern="^.adb(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    adb = f"adb"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{adb} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)


@register(outgoing=True, pattern="^.afh(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    afh = f"afh"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{afh} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.aex(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    aex = f"aex"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{aex} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.aicp(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    aicp = f"aicp"
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
