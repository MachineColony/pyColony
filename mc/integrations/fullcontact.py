import requests
import json


def get_info_from_email(email):
    resp = requests.post('https://integrations.machinecolony.com/fullcontact/from-email',
                         data=json.dumps({'email': email}))
    return resp.text
