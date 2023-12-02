from dotenv import load_dotenv
import os
from typing import TypedDict


class EnvironmentVariables(TypedDict, total=False):
    OPEN_AI_API_KEY: str


def get_environment_variables_from_dotenv() -> EnvironmentVariables:
    # Load environment variables from .env file
    load_dotenv()

    # Create a dictionary with the desired environment variable
    env_vars: EnvironmentVariables = {"OPEN_AI_API_KEY": os.getenv("OPEN_AI_API_KEY", "")}

    return env_vars
