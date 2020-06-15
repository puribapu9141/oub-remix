#"""Fun pligon...for HardcoreUserbot
#\nCode by @Hack12R
#type `.degi` and `.nehi` to see the fun.
#"""
import random, re
#from uniborg.util import admin_cmd
import asyncio
from telethon import events
from userbot.events import register
from asyncio import sleep
import time
from userbot import CMD_HELP

@register(outgoing=True, pattern="^.degi$")
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("wO")
        await asyncio.sleep(0.7)
        await event.edit("dEgI")
        await asyncio.sleep(1)
        await event.edit("tUm")
        await asyncio.sleep(0.8)
        await event.edit("EkBaR")
        await asyncio.sleep(0.9)
        await event.edit("mAnG")
        await asyncio.sleep(1)
        await event.edit("kAr")
        await asyncio.sleep(0.8)
        await event.edit("ToH")
        await asyncio.sleep(0.7)
        await event.edit("dEkHo")
        await asyncio.sleep(1)
        await event.edit("`wO dEgI tUm EkBaR mAnG kAr ToH dEkHo`")

@register(outgoing=True, pattern="^.nehi$")
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("wO")
        await asyncio.sleep(0.7)
        await event.edit("pAkKa")
        await asyncio.sleep(1)
        await event.edit("DeGi")
        await asyncio.sleep(0.8)
        await event.edit("Tu")
        await asyncio.sleep(0.9)
        await event.edit("MaNg")
        await asyncio.sleep(1)
        await event.edit("KaR")
        await asyncio.sleep(0.8)
        await event.edit("tOh")
        await asyncio.sleep(0.7)
        await event.edit("Dekh")
        await asyncio.sleep(1)
        await event.edit("`wO pAkKa DeGi Tu MaNg KaR tOh DeKh`")


CMD_HELP.update({
    "degi":
    ".degi or .nehi\
\nUsage: Sabka Katega."
})    
