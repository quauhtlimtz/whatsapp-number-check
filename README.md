
# WhatsApp Number Checker

This project provides a Python script and a shell script to check if a phone number is registered on WhatsApp using the UltraMsg API. The scripts log the results with detailed and colored logging output, making it easy to see the status of the phone number check.

## Features

- **Check WhatsApp Registration**: Verify if a phone number is registered on WhatsApp using the UltraMsg API.
- **Colored Logging**: Provides colored logging output for better readability and debugging.
- **Error Handling**: Handles generic HTTP request errors and logs them appropriately.
- **Logging to File**: Logs all information to a file (`check_whatsapp.log`) for later review.

## Requirements

- Python 3.x
- `requests` library
- `coloredlogs` library

## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/quauhtlimtz/whatsapp-number-check.git
    cd whatsapp-number-check
    ```

2. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Set Up the Environment Variables**: Update the `check_whatsapp.sh` file with the correct `CHAT_ID`, `TOKEN`, and `INSTANCE_ID`.

    ```sh
    # Variables
    CHAT_ID="+521xxxxxxxxxx"
    TOKEN="your_ultramsg_api_token"
    INSTANCE_ID="your_instance_id"
    LOG_LEVEL="DEBUG"  # Set the desired log level here
    ```

2. **Make the Shell Script Executable**:
    ```sh
    chmod +x check_whatsapp.sh
    ```

3. **Run the Shell Script**:
    ```sh
    ./check_whatsapp.sh
    ```

### Scripts

- **Python Script (`check_whatsapp.py`)**: The main script that makes the API call to check if the phone number is registered on WhatsApp using the UltraMsg API.
- **Shell Script (`check_whatsapp.sh`)**: A helper script to set environment variables and run the Python script.

### Logs

- **Console Logs**: The script logs information to the console with colored output.
- **File Logs**: The script also logs information to a file named `check_whatsapp.log`.

### Example Output

```plaintext
2024-07-04 09:49:43,191 - root - INFO - The number +521xxxxxxxxxx is registered on WhatsApp.
```

## Contributing

Feel free to submit issues, fork the repository, and send pull requests to help improve this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

[Quauhtli Martinez](https://www.linkedin.com/in/quauhtlimtz/)

---

This project makes it easy to verify if a phone number is registered on WhatsApp using the UltraMsg API with a simple and efficient approach with detailed logging. Enjoy using the WhatsApp Number Checker!
