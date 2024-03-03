"""Websocket Coinbase Example."""

import os

from coinbase.websocket import WSBase
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")


def on_message(message: str) -> None:
    """Print message on message."""
    print(message)


def on_error(error: str) -> None:
    """Print message on error."""
    print(error)


def on_close(close_status_code: int, close_msg: str) -> None:
    """Print message on closing connection."""
    print(type(close_status_code))
    print("### closed ###")


def on_open(ws: WSBase) -> None:
    """Print message on opening connection."""
    print("Opened connection")


if __name__ == "__main__":
    ws_client = WSBase(
        api_key=API_KEY,
        api_secret=API_SECRET,
        on_message=on_message,
        verbose=True,
    )
    ws_client.open()
    ws_client.subscribe(["BTC-USD"], ["candles"])
    ws_client.sleep_with_exception_check(10)
    ws_client.close()
