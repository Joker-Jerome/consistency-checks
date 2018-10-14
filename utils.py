import requests
from config import slack_token


def send_slack_notification(message):
    if slack_token() is not None:
        response = requests.post('https://hooks.slack.com/services/' + slack_token(),
                                 json={'text': '> :japanese_ogre: ' + message})

        if response.status_code != 200:
            raise ValueError(
                'Request to slack returned an error %s. The response is:\n%s' % (
                    response.status_code, response.text)
            )
