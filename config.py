from dotenv import load_dotenv
from pathlib import Path
from dataclasses import dataclass
import os


env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


@dataclass
class Config:
    """set config vars from .env file"""

    DEBUG = os.getenv("DEBUG")
    DATABASE = Path(str(os.getenv("DATABASE")))
    SECRET_KEY = os.getenv("SECRET_KEY")
    SSL_CONTEXT = (
        (str(os.getenv("SSL_CONTEXT")).split(","))
        if "," in str(os.getenv("SSL_CONTEXT"))
        else str(os.getenv("SSL_CONTEXT"))
    )


c = Config()
