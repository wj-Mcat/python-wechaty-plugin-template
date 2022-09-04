"""wechaty plugin <foo>"""
from __future__ import annotations
from typing import List, Optional, Union
from dataclasses import dataclass, field
import requests

from wechaty import Message, Contact, Room, get_logger
from wechaty.exceptions import WechatyPluginError
from wechaty.plugin import WechatyPlugin, WechatyPluginOptions


log = get_logger('<Foo>Plugin')


# @dataclass
# class <Foo>PluginOptions(WechatyPluginOptions):
#     """Rasa Rest Connector Options
#     """
#     endpoint: Optional[str] = None
#     conversation_ids: List[str] = field(default_factory=list)


class <Foo>Plugin(WechatyPlugin):
    """<Foo> Plugin"""

    async def on_message(self, msg: Message) -> None:
        """listen message event"""
        pass