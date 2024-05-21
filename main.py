"""
This is a Python script that generates notification using Google webhook.
"""

from json import dumps
from httplib2 import Http

def main():
    """Hangouts Chat incoming webhook quickstart."""
    url = 'put your Google Chat space URL here'
    # Constructing the card content
    card_content = {
        "cards": [
            {
                "sections": [
                    {
                        "widgets": [
                            {
                                'textParagraph': {
                                    'text': 'Hello team, Please fill your Daily Standup Updates'
                                }
                            },
                            {
                                "buttons": [
                                    {
                                        "textButton": {
                                            "text": "Open Document",
                                            "onClick": {
                                                "openLink": {
                                                    "url": "put your document url here"
                                                }
                                            }
                                        }
                                    },
                                    {
                                        "textButton": {
                                            "text": "Join Google Meet",
                                            "onClick": {
                                                "openLink": {
                                                    "url": "put your meeting url here"
                                                }
                                            }
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    }
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(card_content),
    )
    print (response)

if __name__ == '__main__':
    main()
