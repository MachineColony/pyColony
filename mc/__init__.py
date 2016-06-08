import requests


class MC():
    def __init__(self, ctx):
        self._ctx = ctx
        self.api_key = ctx['user']['client_key']
        self.api_secret = ctx['user']['client_secret']

    def _post(self, url, data):
        resp = requests.post(
            url,
            json=data,
            headers = {
                'X-API-Key': self.api_key,
                'X-API-Secret': self.api_secret
            })
        return resp.json()

    def _path_for_model_type(self, model_type):
        if model_type == 'nb':
            return 'bayes/nb'

    def evaluate_model(self, model_id, model_type, data):
        endpoint = 'https://ml.machinecolony.com/{}/{}/evaluate'.format(
            self._path_for_model_type(model_type), model_id)
        return self._post(endpoint, data)

    def create_model(self, model_type, data):
        endpoint = 'https://ml.machinecolony.com/{}/create'.format(
            self._path_for_model_type(model_type))
        return self._post(endpoint, data)

    def evaluate_sentinel(self, model_id, data):
        endpoint = 'https://sentinel.machinecolony.com/models/{}/evaluate'.format(model_id)
        return self._post(endpoint, data)

    def create_sentinel(self, data):
        endpoint = 'https://sentinel.machinecolony.com/create'
        return self._post(endpoint, data)

    def get_keywords(self, string):
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
        return self._post('https://ml.machinecolony.com/codex/keywords', {'data': string})
