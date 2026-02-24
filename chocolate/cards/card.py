from typing import Any
from abc import ABC, abstractmethod
import discord


class Card(ABC):
    @classmethod
    @abstractmethod
    def embed(cls, data: dict[str, Any]) -> discord.Embed:
        pass
