from typing import Dict, Any, TypedDict

from discord import HypeSquadHouse
import re

HYPESQUAD: Dict[str, Any] = {
    "balance": HypeSquadHouse.balance,
    "bravery": HypeSquadHouse.bravery,
    "brilliance": HypeSquadHouse.brilliance
}

HEADERS: Dict[str, str] = {
    "X-Requested-With": "XMLHttpRequest",
}

NITRO_REGEX = re.compile(r"(discord.com/gifts/|discordapp.com/gifts/|discord.gift/)([a-zA-Z0-9]+)")
PRIVNOTE_REGEX = re.compile(r"https://privnote\.com/[a-zA-Z0-9]+#[a-zA-Z0-9]+")
