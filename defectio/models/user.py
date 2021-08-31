from __future__ import annotations

from typing import Optional
from typing import TYPE_CHECKING

from .mixins import Hashable
from ..types.payloads import StatusPayload

if TYPE_CHECKING:
    from ..state import ConnectionState
    from ..types.payloads import UserPayload
    from ..types.websocket import UserUpdate


class Status:
    def __init__(self, status: StatusPayload):
        self.text = status.get("text")
        self.presence = status.get("presence", "Online")

    def __str__(self):
        return f"{self.text} ({self.presence})"

    def __repr__(self) -> str:
        return f"<Status: {self}>"


class PartialUser(Hashable):
    def __init__(
        self,
        id: str,
    ) -> None:
        self.id = id
        self.status = Status(StatusPayload({"presense": "Offline"}))

    def __repr__(self) -> str:
        return f"<PartialUser id={self.id!r}>"

    def __str__(self) -> str:
        return self.id


class User(PartialUser):
    def __init__(self, data: UserPayload, state: ConnectionState):
        self.state = state
        self.id = data["_id"]
        self.name = data["username"]
        self.owner: Optional[str]
        self.bot: bool

        bot = data.get("bot")
        if bot:
            self.bot = True
            self.owner = bot["owner"]
        else:
            self.bot = False
            self.owner = None

        self.badges = data.get("badges", 0)
        self.online = data.get("online", False)
        self.flags = data.get("flags", 0)
        self.status = Status(StatusPayload(data.get("status", {"presense": "Offline"})))

    def _update(self, data: UserUpdate) -> None:
        self.name = data.get("username", self.name)
        self.online = data.get("online", self.online)
        self.badges = data.get("badges", self.badges)
        self.flags = data.get("flags", self.flags)
        if "status" in data:
            self.status = Status(StatusPayload(data["status"]))

    def __repr__(self) -> str:
        return f"<User id={self.id!r} name={self.name!r}>"

    def __str__(self) -> str:
        return self.name
