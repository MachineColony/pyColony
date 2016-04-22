import json
import requests


def create_nb_model(data):
    _data = json.dumps(data)
    resp = requests.post("https://ml.machinecolony.com/bayes/nb/create", data=_data)
    return json.loads(resp.text)


def nb_evaluate(model_id, data):
    _data = json.dumps(data)
    resp = requests.post("https://ml.machinecolony.com/bayes/nb/" + str(model_id) + "/evaluate", data=_data)
    return json.loads(resp.text)
