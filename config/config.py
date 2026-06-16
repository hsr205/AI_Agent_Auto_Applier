from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    linkedin_username: str = Field(...,
                                   description="LinkedIn Username to access the LinkedIn platform via the LinkedIn API")
    linkedin_password: str = Field(...,
                                description="LinkedIn Password to access the LinkedIn platform via the LinkedIn API")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()
