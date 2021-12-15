import asyncio

from .bot import run_polling


def main():
    asyncio.run(run_polling())
