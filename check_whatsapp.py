import os
import sys
import logging
import requests
import coloredlogs

def setup_logging():
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    logging.basicConfig(
        level=getattr(logging, log_level),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("check_whatsapp.log"),
            logging.StreamHandler(sys.stdout)
        ]
    )
    coloredlogs.install(level=log_level, fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def check_whatsapp(chat_id, token):
    url = "https://api.ultramsg.com/instance89422/contacts/check"
    
    querystring = {
        "token": token,
        "chatId": chat_id,
        "nocache": ""
    }

    headers = {'content-type': 'application/x-www-form-urlencoded'}

    logging.debug(f"Request URL: {url}")
    logging.debug(f"Request Headers: {headers}")
    logging.debug(f"Request Params: {querystring}")

    try:
        response = requests.request("GET", url, headers=headers, params=querystring)

        logging.debug(f"Response Status Code: {response.status_code}")
        logging.debug(f"Response Text: {response.text}")

        if response.status_code == 200:
            data = response.json()
            if data['status'] == "valid":
                message = f"The number {chat_id} is registered on WhatsApp."
                logging.info(message)
            else:
                message = f"The number {chat_id} is not registered on WhatsApp."
                logging.info(message)
        else:
            error_message = f"An error occurred: {response.status_code}, {response.text}"
            logging.error(error_message)
    except requests.exceptions.RequestException as e:
        error_message = f"HTTP request failed: {e}"
        logging.error(error_message)

if __name__ == "__main__":
    setup_logging()

    if len(sys.argv) != 3:
        logging.error("Usage: python check_whatsapp.py <chat_id> <token>")
        sys.exit(1)

    chat_id = sys.argv[1]
    token = sys.argv[2]

    check_whatsapp(chat_id, token)