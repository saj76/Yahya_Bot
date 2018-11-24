from datetime import timedelta
import sqlite3

import telethon
from telethon.tl.types import InputPeerChannel, ChannelParticipantsAdmins
from telethon import TelegramClient, events, sync, client
import socks
from telethon import utils
import requests

api_ID = 627730
api_hash = 'f82878060252f2e061451349aac6436f'

host = '127.0.0.1'  # a valid host
port = 9150  # a valid port
proxy = (socks.SOCKS5, host, port)

client_Yahya = TelegramClient("Test Session", api_ID, api_hash
                              , proxy=(socks.SOCKS5, '127.0.0.1', 9150, True, 'log', 'pass'),
                              # ,timeout=timedelta(seconds=10)
                              )
client_Yahya.start()

groups = dict()
dialogs = client_Yahya.get_dialogs()
members = set()
for dialog in dialogs:
    # print(type(dialog.entity), dialog.name)

    if type(dialog.entity) == telethon.tl.types.Channel and dialog.entity.broadcast is not True:
        groups[dialog] = []
        for member in client_Yahya.iter_participants(dialog):
            members.add(member.id)
            groups[dialog].append(member)

groups = (list(groups.keys()))
print(groups)
non_admins = set()
for group in groups:
    groups_admin = client_Yahya.get_participants('https://t.me/joinchat/BkrTD0qLg1rSB3sbLDxg9g', filter=ChannelParticipantsAdmins)
    print(group)
    participants = list(client_Yahya.get_participants(group))
    for participant in participants:
        if participant not in groups_admin:
            non_admins.add(participant.id)


@client_Yahya.on(events.NewMessage(chats='https://t.me/IRANCOIN24'))
async def handler(event):
    for contact in groups:
        await client_Yahya.forward_messages(contact, event.message)


client_Yahya.run_until_disconnected()

