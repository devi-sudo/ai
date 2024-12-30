
# URL of the website to monitor
# Replace with your website URL
import requests
import time
import os

# Telegram bot configuration
TELEGRAM_BOT_TOKEN = "7586502137:AAETluyDL-emEXAgi0hq0Gf3wRLkIbf91Wk" # Replace with your bot token
TELEGRAM_CHAT_ID = -1001837030838      # Replace with your chat ID

# Get URL and interval from the user
WEBSITE_URL = input("Enter the website URL to monitor (with https://): ").strip()
CHECK_INTERVAL = int(input("Enter the check interval (in seconds): "))
def send_telegram_alert(message):
    """Send an alert message to Telegram."""
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("✅ Telegram alert sent successfully.")
        else:
            print(f"⚠️ Failed to send Telegram alert. Status code: {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"❌ Error sending Telegram alert: {str(e)}")

def check_website():
    """Check the website's status."""
    try:
        response = requests.get(WEBSITE_URL, timeout=10)
        if response.status_code == 200:
            status = f"[{time.ctime()}] Website is UP."
        else:
            status = f"[{time.ctime()}] Website is DOWN. Status code: {response.status_code}"
            send_telegram_alert(f"🚨 **Alert**: {WEBSITE_URL} is DOWN. Status code: {response.status_code}")
        print(status)

        # Log the status to a file
        with open("uptime_log.txt", "a") as log_file:
            log_file.write(status + "\n")
    except requests.exceptions.RequestException as e:
        status = f"[{time.ctime()}] Website is DOWN. Error: {str(e)}"
        print(status)

        # Log the error to a file
        with open("uptime_log.txt", "a") as log_file:
            log_file.write(status + "\n")

        # Send a Telegram alert
        send_telegram_alert(f"🚨 **Alert**: {WEBSITE_URL} is DOWN. Error: {str(e)}")

if __name__ == "__main__":
    # Validate Telegram credentials
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("❌ Telegram bot token or chat ID is missing. Set these values before running the script.")
        exit(1)

    print(f"Starting uptime monitor for {WEBSITE_URL}...")
    while True:
        check_website()
        time.sleep(CHECK_INTERVAL)
