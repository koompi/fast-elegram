from typing import List
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon.errors.rpcerrorlist import PeerIdInvalidError
from telethon import TelegramClient

from fastapi import HTTPException


async def get_entity(
    peer_id,
    client
):

    try:
        try:
            entity = await client.get_entity(PeerUser(int(peer_id)))
        except Exception:
            try:
                entity = await client.get_entity(PeerChannel(int(peer_id)))
            except Exception:
                entity = await client.get_entity(PeerChat(int(peer_id)))
    except Exception:
        try:
            entity = await client.get_entity(peer_id)
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid Peer Id")
    return entity


async def get_list_entity(
    peer_ids: List[str],
    client: TelegramClient
):
    entitys = []
    for peer_id in peer_ids:
        try:
            try:
                entity = await client.get_entity(PeerUser(int(peer_id)))
            except Exception:
                try:
                    entity = await client.get_entity(
                        PeerChannel(int(peer_id)))
                except Exception:
                    entity = await client.get_entity(
                        PeerChat(int(peer_id)))
        except Exception:
            try:
                entity = await client.get_entity(peer_id)
                entitys.append(entity)
            except PeerIdInvalidError:
                raise HTTPException(status_code=400, detail="Invalid Peer Id")
            except Exception:
                raise HTTPException(
                    status_code=400,
                    detail="something went wrong")
    return entitys
