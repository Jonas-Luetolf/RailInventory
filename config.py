from uuid import uuid4
from dotenv import load_dotenv
from pathlib import Path
from dataclasses import dataclass
import os

env_path = Path(".") / "var" / ".env"
load_dotenv(dotenv_path=env_path)


@dataclass
class Config:
    """set config vars from .env file"""

    DEBUG = os.getenv("DEBUG")
    DATABASE = Path(str(os.getenv("DATABASE")))
    SECRET_KEY = uuid4().hex
