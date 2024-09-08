import os
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    app_name: str = 'Rest API'

    db_host: str = Field(alias='DB_HOST')
    db_user: str = Field(alias="DB_USER")
    db_port: int = Field(alias="DB_PORT")
    db_pass: str = Field(alias="DB_PASS")
    db_name: str = Field(alias="DB_NAME")

    class Config:
        env_file = f"{os.path.dirname(os.path.abspath(__file__))}/../.env"