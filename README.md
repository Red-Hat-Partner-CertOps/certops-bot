# Google Webhook Notification Generator

This Python script facilitates the generation of notifications using Google webhook for Hangouts Chat. It constructs a card with specified content and sends it to the designated Google Chat space URL.

## Prerequisites

Before running the script, ensure you have the following:
- Python installed on your system
- An active Google Chat space URL
- URLs for the document and meeting where applicable, to be included in the card content

## Usage

1. Clone this repository to your local machine or download the `main.py` file.
2. Open the `main.py` file in a text editor.
3. Replace placeholders with your actual Google Chat space URL, document URL, and meeting URL where indicated.
4. Save the changes.
5. Run the script by executing `python main.py` in your terminal or command prompt.

## Script Overview

- The `main()` function constructs a JSON payload representing a card with specified content, including a text paragraph and buttons.
- The constructed payload is sent as an HTTP POST request to the provided Google Chat space URL.
- Upon successful execution, the script prints the HTTP response.

## Customization

- Modify the text content within the `card_content` dictionary to suit your notification message requirements.
- Adjust the button text and URLs to tailor the card content to your specific use case.

## License

This project is licensed under the [Apache License 2.0](LICENSE).

