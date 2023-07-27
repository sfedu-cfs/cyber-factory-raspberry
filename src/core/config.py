import configparser
from dataclasses import dataclass

parser = configparser.ConfigParser()
parser.read("/home/lowqa/WORK/dev_repositories/factory_analyzer/src/settings.ini")


@dataclass
class Config:
    base_url = parser["api"]["base_url"]
    email = parser["login"]["email"]
    password = parser["login"]["password"]


config = Config()
