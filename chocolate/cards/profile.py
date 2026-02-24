from typing import Any
from .card import Card
import discord


class ProfileCard(Card):
    @classmethod
    def embed(cls, data: dict[str, Any]) -> discord.Embed:

        card = discord.Embed(
            color=cls.card_color(data),
            title=data['usual_full_name'],
            url=f"https://intra.42.fr/users/{data['login']}"
        )

        card.set_thumbnail(url=data['image']['link'])

        cls.login_field(card, data)
        cls.campus_field(card, data)
        if not cls.cc_grade(card, data):
            cls.pool_grade(card, data)
        cls.wallet_field(card, data)

        return card

    @staticmethod
    def cc_grade(card: discord.Embed, data: dict) -> bool:
        user_cursus = data["cursus_users"]
        cc_cursus = [
            cursus for cursus in user_cursus if cursus['grade'] == 'Cadet'
        ]
        if cc_cursus:
            card.add_field(
                name="Level:",
                value=cc_cursus[-1]['level'],
            )
            return True
        return False

    @staticmethod
    def pool_grade(card: discord.Embed, data: dict) -> None:
        user_cursus = data["cursus_users"]
        piscin_cursus = [
            cursus for cursus in user_cursus if cursus['grade'] == 'Pisciner'
        ]
        if piscin_cursus:
            card.add_field(
                name="Piscin Level:",
                value=piscin_cursus[-1]['level']
            )

    @staticmethod
    def points_field(card: discord.Embed, data: dict) -> None:
        card.add_field(
            name="Points:",
            value=data["correction_point"]
        )

    @staticmethod
    def wallet_field(card: discord.Embed, data: dict) -> None:
        wallet = data["wallet"]
        if wallet:
            card.add_field(
                name="Wallet:",
                value=f"{wallet}💸",
            )

    @staticmethod
    def campus_field(card: discord.Embed, data: dict[str, Any]) -> None:
        campuses = data['campus']
        campuses_name = [campus["name"] for campus in campuses]
        card.add_field(
            name="Campus:" if len(campuses_name) == 1 else "Campuses:",
            value="\n".join(campuses_name)
        )

    @staticmethod
    def card_color(data: dict) -> discord.Color:
        kind = data["kind"]
        match kind.lower():
            case "student":
                return discord.Color.brand_green()
            case "admin":
                return discord.Color.purple()
        print(kind)
        return discord.Color.red()

    @staticmethod
    def login_field(card: discord.Embed, data: dict) -> None:
        card.add_field(
            name=f"{data['kind'].capitalize()}:",
            value=f"`{data['login']}`",
            inline=False
        )
