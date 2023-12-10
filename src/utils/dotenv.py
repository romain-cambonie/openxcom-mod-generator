from dotenv import load_dotenv
import os
from typing import TypedDict


class EnvironmentVariables(TypedDict, total=False):
    OPEN_AI_API_KEY: str
    WORKING_DIRECTORY: str
    LANGUAGE_DIRECTORY: str
    LANGUAGE_LOCALE: str


def get_environment_variables_from_dotenv() -> EnvironmentVariables:
    # Load environment variables from .env file
    load_dotenv()

    # Create a dictionary with the desired environment variable
    env_vars: EnvironmentVariables = {
        "OPEN_AI_API_KEY": os.getenv("OPEN_AI_API_KEY", ""),
        "WORKING_DIRECTORY": os.getenv("WORKING_DIRECTORY", ""),
        "LANGUAGE_DIRECTORY": os.getenv("LANGUAGE_DIRECTORY", ""),
        "LANGUAGE_LOCALE": os.getenv("LANGUAGE_LOCALE", ""),
    }

    return env_vars
