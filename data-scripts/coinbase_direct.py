from coinbase.websocket import WSBase
import json
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

def on_message(message):
    print(message)

def on_error(error):
    print(error)

def on_close(close_status_code, close_msg):
    print("### closed ###")

def on_open(ws):
    print("Opened connection")

if __name__ == "__main__":
    ws_client = WSBase(
        api_key=API_KEY, 
        api_secret=API_SECRET, 
        on_message=on_message, 
        verbose=True
    )
    ws_client.open()
    ws_client.subscribe(["BTC-USD"], ["candles"])
    ws_client.sleep_with_exception_check(10)
    ws_client.close()