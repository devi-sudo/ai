import requests
import time

# URL of the website to monitor
WEBSITE_URL = "https://fine-sunny-weeder.glitch.me/"  # Replace with your website URL

# Time interval for checking (in seconds)
CHECK_INTERVAL = 180  # Check every 5 minutes

def check_website():
    try:
        response = requests.get(WEBSITE_URL, timeout=10)
        if response.status_code == 200:
            print(f"[{time.ctime()}] Website is UP.")
        else:
            print(f"[{time.ctime()}] Website is DOWN. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[{time.ctime()}] Website is DOWN. Error: {str(e)}")

if __name__ == "__main__":
    print(f"Starting uptime monitor for {WEBSITE_URL}...")
    while True:
        check_website()
        time.sleep(CHECK_INTERVAL)
