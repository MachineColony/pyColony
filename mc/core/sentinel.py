# Interface to the Sentinel API for anomaly detection
import requests


def evaluate(data, model_id):
    return requests.post("https://sentinel.machinecolony.com/models/%s/evaluate" % model_id, data=data)


def create_model(data):
    return requests.post("https://sentinel.machinecolony.com/create", data=data)
