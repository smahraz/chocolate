from .card import Card
from discord import Embed, Color


class PermissionErrorCard(Card):
    @classmethod
    def embed(cls, description: str) -> Embed:
        return Embed(
            color=Color.dark_red(),
            title="Permission Error",
            description=description,
        )


class ProfileNotFoundCard(Card):
    @classmethod
    def embed(cls, description: str) -> Embed:
        return Embed(
            color=Color.dark_magenta(),
            title="Login Not Found",
            description=description
        )
