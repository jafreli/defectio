"""
Revolt API Wrapper
~~~~~~~~~~~~~~~~~~~

A python wrapper for the Revolt API.

:copyright: (c) 2021-present Darkflame72
:license: MIT, see LICENSE for more details.

"""

__title__ = "defectio"
__author__ = "Darkflame72"
__license__ = "MIT"
__copyright__ = "Copyright 2021-present Darkflame72"
__version__ = "0.1.4a"

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

import logging
from typing import NamedTuple, Literal

from .client import Client
from .models import (
    Message,
    User,
    Server,
    Member,
    Role,
    RawMessageDeleteEvent,
    RawMessageUpdateEvent,
    TextChannel,
    VoiceChannel,
    GroupChannel,
    DMChannel,
    Category,
    Status,
)
from .models import abc
from . import utils
from .errors import (
    DefectioException,
    ClientException,
    GatewayNotFound,
    HTTPException,
    Forbidden,
    RevoltServerError,
    InvalidArgument,
    InvalidData,
    LoginFailure,
)


__all__ = (
    "__title__",
    "__author__",
    "__license__",
    "__copyright__",
    "__version__",
    "Client",
    "Message",
    "User",
    "Server",
    "Member",
    "abc",
)


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(
    major=0, minor=1, micro=4, releaselevel="alpha", serial=0
)

logging.getLogger(__name__).addHandler(logging.NullHandler())
