# Interface to the Sentinel API for anomaly detection
import requests


def evaluate(data, model_id):
    _data = {'data': data}
    return requests.post("https://sentinel.machinecolony.com/models/%s/evaluate" % model_id, data=_data)


def create_model(data):
    _data = {'data': data}
    return requests.post("https://sentinel.machinecolony.com/create", data=_data)
