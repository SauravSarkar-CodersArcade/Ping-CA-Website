import requests
import os

URL = os.getenv("URL")  # Get URL from environment variable
try:
    response = requests.get(URL)
    print(f"Successfully pinged {URL}, Status Code: {response.status_code}")
except Exception as e:
    print(f"Error pinging {URL}: {e}")
