import os
from dotenv import load_dotenv
from binance.um_futures import UMFutures
from binance.error import ClientError

# Load .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
BASE_URL = os.getenv("BASE_URL", "https://fapi.binance.com")

print("Using BASE_URL:", BASE_URL)

try:
    client = UMFutures(key=API_KEY, secret=API_SECRET, base_url=BASE_URL)

    # Just get account balance (safe, no orders)
    balances = client.balance()

    print("✅ API key works! Your Futures balances:")
    for b in balances:
        print(b)

except ClientError as e:
    print("❌ ClientError:", e.error_message)
    print("Code:", e.status_code, "Msg:", e.error_message)
except Exception as e:
    print("❌ Other error:", e)
