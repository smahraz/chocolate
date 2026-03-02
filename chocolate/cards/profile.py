from datetime import datetime
from typing import Any
from .card import Card
from discord import Embed, Color


class ProjectCard(Card):
    @classmethod
    def embed(cls, data: dict[str, Any]) -> Embed:
        card = Embed(
            title=data["project"]["name"],
            color=cls.card_color(data),
            description=data['user']['login']
        )

        card.set_thumbnail(url=data["user"]["image"]["link"])
        cls.marked_at(card, data)

        cls.project_grade(card, data)
        return card

    @staticmethod
    def card_color(data: dict) -> Color:
        return Color.green() if data["validated?"] else Color.red()

    @staticmethod
    def project_grade(card: Embed, data: dict) -> None:
        value = str(data['final_mark'])
        value += " ✅" if data["validated?"] else " ❌"
        card.add_field(name="Grade:", value=value)

    @staticmethod
    def marked_at(card: Embed, data: dict) -> None:
        time = datetime.fromisoformat(data['marked_at'].rstrip("Z"))
        card.set_footer(text=time.strftime("%d/%m/%Y %I:%M%p"))


class ProfileCard(Card):
    @classmethod
    def embed(cls, data: dict[str, Any]) -> Embed:

        card = Embed(
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
    def cc_grade(card: Embed, data: dict) -> bool:
        user_cursus = data["cursus_users"]
        cc_cursus = [
            cursus for cursus in user_cursus if cursus['grade'] == 'Cadet'
        ]
        if cc_cursus:
            card.add_field(
                name="Level:",
                value=round(cc_cursus[-1]['level'], 2)
            )
            return True
        return False

    @staticmethod
    def pool_grade(card: Embed, data: dict) -> None:
        user_cursus = data["cursus_users"]
        piscin_cursus = [
            cursus for cursus in user_cursus if cursus['grade'] == 'Pisciner'
        ]
        if piscin_cursus:
            card.add_field(
                name="Piscin Level:",
                value=round(piscin_cursus[-1]['level'], 2)
            )

    @staticmethod
    def points_field(card: Embed, data: dict) -> None:
        card.add_field(
            name="Points:",
            value=data["correction_point"]
        )

    @staticmethod
    def wallet_field(card: Embed, data: dict) -> None:
        wallet = data["wallet"]
        if wallet:
            card.add_field(
                name="Wallet:",
                value=f"{wallet}💸",
            )

    @staticmethod
    def campus_field(card: Embed, data: dict[str, Any]) -> None:
        campuses = data['campus']
        campuses_name = [campus["name"] for campus in campuses]
        card.add_field(
            name="Campus:" if len(campuses_name) == 1 else "Campuses:",
            value="\n".join(campuses_name)
        )

    @staticmethod
    def card_color(data: dict) -> Color:
        kind = data["kind"]
        match kind.lower():
            case "student":
                return Color.brand_green()
            case "admin":
                return Color.purple()
        print(kind)
        return Color.red()

    @staticmethod
    def login_field(card: Embed, data: dict) -> None:
        card.add_field(
            name=f"{data['kind'].capitalize()}:",
            value=f"`{data['login']}`",
            inline=False
        )
