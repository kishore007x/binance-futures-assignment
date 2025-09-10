

import os
from dotenv import load_dotenv
from binance.um_futures import UMFutures  


load_dotenv()


API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
BASE_URL = os.getenv("BASE_URL", "https://fapi.binance.com")


def get_client() -> UMFutures:
    """Return authenticated Binance Futures client"""
    if not API_KEY or not API_SECRET:
        raise RuntimeError("API keys missing in .env")
    return UMFutures(key=API_KEY, secret=API_SECRET, base_url=BASE_URL)
