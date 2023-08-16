from logging import config as logging_config

from pydantic import BaseSettings

from core.logger import LOGGING

logging_config.dictConfig(LOGGING)


class Settings(BaseSettings):
    competitors2_path: str = './competitors2.json'
    results_path: str = './results_RUN.txt'    


settings = Settings()
