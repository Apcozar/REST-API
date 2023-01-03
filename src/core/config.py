from pydantic import BaseSettings


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    access_token_expires_minutes = 45

    class Config:
        env_file = ".env"

settings = Settings()