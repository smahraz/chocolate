from pydantic import BaseModel, Field, field_validator, ValidationError


class BotConfig(BaseModel):
    moderators: list[str] = Field(min_length=1)
    devs: list[str] = Field(min_length=1)

    @field_validator('moderators', 'devs', mode="after")
    @classmethod
    def moderators_(cls, moderators: list[str]) -> list[str]:
        for role in moderators:
            if not 1 <= len(role) <= 100:
                raise ValueError("Role name is so long")
            if '\n' in role:
                raise ValueError("Line breaks in role name")
            if '\t' in role:
                raise ValueError("Line breaks in role name")
        return moderators


try:
    with open("config.json", 'r') as config_file:
        bot_config = BotConfig.model_validate_json(config_file.read())
except (FileNotFoundError, IsADirectoryError, PermissionError) as e:
    print(f"{e.__class__.__name__}: Could not open config.json")
    exit(1)

except ValidationError:
    print("ValidationError: parsing error")
    exit(1)

if __name__ == "__main__":
    print(bot_config.moderators)
