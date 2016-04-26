import json
import requests


def get_keywords(string):
    """
    Get a list of keywords for the given string.

    :param string:
    :return:
        Dict:
        {
            data: {
                results: Array. List of keywords for the given string.
            }
        }
    """
    _data = json.dumps({'data': string})
    res = requests.post("https://ml.machinecolony.com/codex/keywords", data=_data)
    return json.loads(res.text)
