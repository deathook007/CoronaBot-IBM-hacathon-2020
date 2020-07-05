import requests
import json
import logging
DEFAULT_SLACK_WEBHOOK = 'https://hooks.slack.com/services/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'
#DEFAULT_SLACK_WEBHOOK = 'https://hooks.slack.com/services/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'
from auth import DEFAULT_SLACK_WEBHOOK

HEADERS = {
    'Content-type': 'application/json'
}


def slacker(webhook_url=DEFAULT_SLACK_WEBHOOK):
#def slacker(webhook_url= 'https://hooks.slack.com/services/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'):
    def slackit(msg):
        logging.info('Sending {msg} to slack'.format(msg=msg))
        payload = { 'text': msg }
        return requests.post(webhook_url, headers=HEADERS, data=json.dumps(payload))
    return slackit
#https://hooks.slack.com/services/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
#https://hooks.slack.com/services/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