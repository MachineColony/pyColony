import requests
import json


def get_messages(user_id):
    response = requests.post("https://integrations.machinecolony.com/google/gmail/get-messages",
                             data=json.dumps({'user_id': user_id}))
    return response


def get_labels(user_id):
    response = requests.post("https://integrations.machinecolony.com/google/gmail/get-labels",
                             data=json.dumps({'user_id': user_id}))
    return response
