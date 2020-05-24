# (c) @UniBorg
# Original written by @UniBorg edit by @I_m_Rock

from telethon import events
import asyncio
from collections import deque
from userbot.events import register

@register(outgoing=True, pattern="^.finger")
async def port_kalp(event):
	if event.fwd_from:
		return
	deq = deque(list("✌️🤘🤙🤞🖖☝️👆"))
	for _ in range(48):
		await asyncio.sleep(1)
		await event.edit("".join(deq))
		deq.rotate(1)
