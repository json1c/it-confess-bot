import os
from dataclasses import MISSING, dataclass, field, fields
from typing import List, Optional

import toml
from PIL import Image, ImageFont


@dataclass
class ConfigSettings:
    font_path: str
    background_path: str
    parables_path: str


@dataclass
class ConfigAPI:
    api_url: str


@dataclass
class ConfigBot:
    token: str


@dataclass
class ConfigWeb:
    listen_port: int
    listen_ip: str


@dataclass
class Config:
    bot: ConfigBot
    api: ConfigAPI
    settings: ConfigSettings
    web: ConfigWeb

    _cached_background: Optional[Image.Image] = field(default=None, init=False, repr=False)
    _cached_font: Optional[ImageFont.FreeTypeFont] = field(default=None, init=False, repr=False)
    _parables_list: List[str] = field(default_factory=list, init=False, repr=False)
    
    @classmethod
    def parse(cls, data: dict) -> "Config":
        sections = {}

        for section in fields(cls):
            if section.name.startswith("_"):
                continue

            pre = {}
            current = data[section.name]

            for field in fields(section.type):
                if field.name in current:
                    pre[field.name] = current[field.name]
                elif field.default is not MISSING:
                    pre[field.name] = field.default
                else:
                    raise ValueError(
                        f"Missing field {field.name} in section {section.name}"
                    )

            sections[section.name] = section.type(**pre)

        return cls(**sections)


def parse_config(config_file: str) -> Config:
    if not os.path.isfile(config_file) and not config_file.endswith(".toml"):
        config_file += ".toml"

    if not os.path.isfile(config_file):
        raise FileNotFoundError(f"Config file not found: {config_file} no such file")

    with open(config_file, "r") as f:
        data = toml.load(f)

    return Config.parse(dict(data))
