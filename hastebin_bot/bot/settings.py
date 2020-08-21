from pathlib import Path
import typing
import os

from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types
from aiogram_oop_framework.core.project import Project, ProjectStructure
from aiogram.contrib.fsm_storage.memory import MemoryStorage

PATH = Path(__file__).parent.parent.parent
PROJECT_NAME = "hastebin_bot"
pr: Project = Project(PROJECT_NAME, PATH)
struc: ProjectStructure = ProjectStructure(pr)
struc.include('bot.views.commands')
pr.structure = struc

PROJECT: Project = pr

AUTO_REGISTER_VIEWS = True


TELEGRAM_BOT_TOKEN: str = os.environ['HASTEBIN_BOT_TOKEN']

MIDDLEWARES: typing.List[BaseMiddleware.__class__] = []

MEMORY_STORAGE = MemoryStorage()

PARSE_MODE = types.ParseMode.HTML
