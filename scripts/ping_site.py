import requests
import os
import datetime

URL = os.getenv("URL")  # Get URL from environment variable

print(f"Running ping at: {datetime.datetime.utcnow()} UTC")
try:
    response = requests.get(URL)
    print(f"Successfully pinged {URL}, Status Code: {response.status_code}")
except Exception as e:
    print(f"Error pinging {URL}: {e}")

