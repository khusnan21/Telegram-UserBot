# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#
# You can find misc modules, which dont fit in anything xD

""" Userbot module for other small commands. """

from random import randint
from time import sleep
import os
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.random")
async def randomise(items):
    """ For .random command, get a random item from the list of items. """
    if not items.text[0].isalpha() and items.text[0] not in ("/", "#", "@", "!"):
        itemo = (items.text[8:]).split()
        index = randint(1, len(itemo) - 1)
        await items.edit("**Query: **\n`" + items.text[8:] + "`\n**Output: **\n`" + itemo[index] + "`")

@register(outgoing=True, pattern="^.sleep( [0-9]+)?$")
async def sleepybot(time):
    """ For .sleep command, let the userbot snooze for a few second. """
    message = time.text
    if not message[0].isalpha() and message[0] not in ("/", "#", "@", "!"):
        if " " not in time.pattern_match.group(1):
            await time.reply("Syntax: `.sleep [seconds]`")
        else:
            counter = int(time.pattern_match.group(1))
            await time.edit("`I am sulking and snoozing....`")
            sleep(2)
            if BOTLOG:
                await time.client.send_message(
                    BOTLOG_CHATID,
                    "You put the bot to sleep for " + str(counter) + " seconds",
                )
            sleep(counter)


@register(outgoing=True, pattern="^.shutdown$")
async def killdabot(event):
    """ For .shutdown command, shut the bot down."""
    if not event.text[0].isalpha():
        await event.edit("`Goodbye *Windows XP shutdown sound*....`")
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#SHUTDOWN \n"
                "Bot shut down")
        await event.client.disconnect()

# Copyright(c) Kandnub | 2019
@register(outgoing=True, pattern="^.restart$")
async def revivedabot(restart):
    """ For .restart command, restart the bot down."""
    if not restart.text[0].isalpha():
        await restart.edit("`BRB... *PornHub intro*`")
        bye = os.getpid()
        bash = f"#!/bin/bash/\nkill -9 {bye}\npython3 -m userbot"
        f = open("restart.sh", "w+")
        f.write(bash)
        f.close()
        os.popen("bash restart.sh")

@register(outgoing=True, pattern="^.support$")
async def bot_support(wannahelp):
    """ For .support command, just returns the group link. """
    if not wannahelp.text[0].isalpha() and wannahelp.text[0] not in ("/", "#", "@", "!"):
        await wannahelp.edit("Join the userbot community: @userbot_support")

@register(outgoing=True, pattern="^.creator$")
async def creator(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("[AvinashReddy3108](https://t.me/AvinashReddy3108)")

@register(outgoing=True, pattern="^.readme$")
async def reedme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("[README.md](https://github.com/AvinashReddy3108/Telegram-UserBot/blob/master/README.md)")

#
# Copyright (c) Gegham Zakaryan | 2019
#
@register(outgoing=True, pattern="^.repeat (.*) (.*)")
async def repeat(rep):
    if not rep.text[0].isalpha() and rep.text[0] not in ("/", "#", "@", "!"):
        replyCount = int(rep.pattern_match.group(1))
        toBeRepeated = rep.pattern_match.group(2)

        replyText = toBeRepeated + "\n"

        for i in range(0, replyCount-1):
            replyText += toBeRepeated + "\n"

        await rep.edit(replyText)

@register(outgoing=True, pattern="^.repo$")
async def repo_is_here(wannasee):
    """ For .repo command, just returns the repo URL. """
    if not wannasee.text[0].isalpha() and wannasee.text[0] not in ("/", "#", "@", "!"):
        await wannasee.edit("[SOURCE CODE](https://github.com/AvinashReddy3108/Telegram-UserBot)")

CMD_HELP.update({
    'random': '.random <item1> <item2> ... <itemN>\
\nUsage: Get a random item from the list of items.'
})
CMD_HELP.update({
    'sleep': '.sleep <seconds>\
\nUsage: Userbots get tired too. Let yours snooze for a few seconds.'
})
CMD_HELP.update({
    "shutdown": ".shutdown\
\nUsage: Sometimes you need to restart your bot. Sometimes you just hope to\
hear Windows XP shutdown sound... but you don't."
})
CMD_HELP.update({
    'support': ".support\
\nUsage: If you need help, use this command."
})
CMD_HELP.update({
    'repo': '.repo\
\nUsage: If you are curious what makes the userbot work, this is what you need.'
})
CMD_HELP.update({
    "readme": "Read nibba READ !!"
})
CMD_HELP.update({
    "creator": "Know who created this awesome userbot !!"
})
CMD_HELP.update({
    "repeat": ".repeat <no.> <text>\nRepeats a text number of times."
})
CMD_HELP.update({
    "restart": "Restart the bot !!"
})
