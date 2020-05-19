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

@register(outgoing=True, pattern="^.aosip(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    aosip = f"aosip"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{aosip} {link}')
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
              await conv.send_message(f'/{aicp} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.reapk(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    reapk = f"reapk"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{reapk} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.am(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    am = f"am"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{am} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.aqua(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    aqua = f"aqua"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{aqua} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.arrow(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    arrow = f"arrow"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{arrow} {link}')
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

@register(outgoing=True, pattern="^.asus(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    asus = f"asus"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{asus} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.bootleg(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    booleg = f"bootleg"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{bootleg} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.caf(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    caf = f"caf"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{caf} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.candy(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    candy = f"candy"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{candy} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.carbon(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    carbon = f"carbon"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{carbon} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.top(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    top = f"top"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{top} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.popular(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    popular = f"popular"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{popular} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.apk(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    apk = f"apk"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{apk} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.discover(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    discover = f"discover"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{discover} {link}')
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

@register(outgoing=True, pattern="^.colt(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    colt = f"colt"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{colt} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.cosp(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    cosp = f"cosp"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{cosp} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.crdroid(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    crDroid = f"crdroid"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{crdroid} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)

@register(outgoing=True, pattern="^.ddump(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@android_helper_bot"
    ddump = f"ddump"
    await event.edit("```Processing```")
    async with bot.conversation("@android_helper_bot") as conv:
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=995271804))
              await conv.send_message(f'/{ddump} {link}')
              response = await response
          except YouBlockedUserError:
              await event.reply("```Unblock @android_helper_bot plox```")
              return
          else:
             await event.delete()
             await bot.forward_messages(event.chat_id, response.message)
