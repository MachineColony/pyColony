import json
import requests


def summarize(text):
    response = requests.post('https://deeplearn.machinecolony.com/text/summarize', json={'text': text})
    return json.loads(response.text)


def summarize_batch(text_list):
    response = requests.post('https://deeplearn.machinecolony.com/text/summarize-batch', json={'text_list': text_list})
    return json.loads(response.text)


def get_entities(text):
    response = requests.post('https://deeplearn.machinecolony.com/text/get-entities', json={'text': text})
    return json.loads(response.text)
