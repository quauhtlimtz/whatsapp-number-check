#!/bin/bash

# Variables
CHAT_ID="+5216421179635"
TOKEN="dzs0ya9edahg3opk"
LOG_LEVEL="INFO"  # Set the desired log level here

# Export the LOG_LEVEL variable
export LOG_LEVEL

# Run the Python script
python check_whatsapp.py "$CHAT_ID" "$TOKEN"