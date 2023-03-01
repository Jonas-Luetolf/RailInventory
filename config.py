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
    SSL_CONTEXT = (
        (os.getenv("SSL_CONTEXT").split(","))
        if "," in os.getenv("SSL_CONTEXT")
        else os.getenv("SSL_CONTEXT")
    )


c = Config()
