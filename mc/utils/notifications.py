import json
import requests


def send_email(email_address, message, subject=None):
    _data = {"email_address": email_address, "message": message, "subject": subject}
    return requests.post("https://api.machinecolony.com/bot-utils/send-email", data=json.dumps(_data))
