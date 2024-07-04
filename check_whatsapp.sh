#!/bin/bash

# Variables
CHAT_ID="+521xxxxxxxxxx" # The phone number to check with country area code
TOKEN="your_token"
LOG_LEVEL="INFO"  # Set the desired log level here

# Export the LOG_LEVEL variable
export LOG_LEVEL

# Run the Python script
python check_whatsapp.py "$CHAT_ID" "$TOKEN"
