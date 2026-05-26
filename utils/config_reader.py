import json
from pathlib import Path


class ConfigReader:
    """
    Reads project configuration from config/config.json.
    This helps keep test settings separate from automation code.
    """

    @staticmethod
    def get_config():
        config_path = Path(__file__).parent.parent / "config" / "config.json"

        with open(config_path, "r", encoding="utf-8") as config_file:
            return json.load(config_file)

    @staticmethod
    def get_base_url():
        return ConfigReader.get_config()["base_url"]

    @staticmethod
    def get_browser():
        return ConfigReader.get_config()["browser"]

    @staticmethod
    def get_timeout():
        return ConfigReader.get_config()["timeout"]

    @staticmethod
    def is_headless():
        return ConfigReader.get_config()["headless"]