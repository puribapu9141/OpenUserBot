# (c) @UniBorg
# Original written by @UniBorg edit by @PM_The_Angry

from telethon import events
import asyncio
from collections import deque
from userbot.events import register

@register(outgoing=True, pattern="^.pmlob")
async def port_pmlob(event):
	if event.fwd_from:
		return
	deq = deque(list("โค๏ธ๐งก๐’๐’๐’๐’๐–ค"))
	for _ in range(48):
		await asyncio.sleep(1)
		await event.edit("".join(deq))
		deq.rotate(1)
    
