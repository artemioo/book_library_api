from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_URL: str
    DB_ECHO: bool = True  # отвечает за вывод логов sql в консоль
    # RELOAD: bool = True
    # DEBUG: bool = False

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()