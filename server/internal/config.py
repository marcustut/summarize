# Author: Lee Kai Yang

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Summarize API"
    hugging_face_api_token: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
