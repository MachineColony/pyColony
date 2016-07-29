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
            headers={
                'X-API-Key': self.api_key,
                'X-API-Secret': self.api_secret
            })
        return resp.json()

    def set_auth(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

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

    def create_auto_regression(self, data):
        return self._post('https://ml.machinecolony.com/regression/auto/create', data)

    def create_auto_classifier(self, data):
        return self._post('https://ml.machinecolony.com/classification/auto/create', data)

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

    def send_email(self, email_address, message, subject=None):
        _data = {"email_address": email_address, "message": message, "subject": subject}
        return self._post("https://api.machinecolony.com/bot-utils/send-email", _data)

    def get_gmail_messages(self, user_id):
        return self._post("https://integrations.machinecolony.com/google/gmail/get-messages", {'user_id': user_id})

    def get_gmail_labels(self, user_id):
        return self._post("https://integrations.machinecolony.com/google/gmail/get-labels", {'user_id': user_id})

    def trace(self, bot_instance_guid, message):
        """
        Trace steps to explain what a bot is doing, log out important data to a dashboard module, etc.

        :param bot_instance_id:
        :param message:
            Any valid string.
        :return:
        """
        return self._post("https://trace.machinecolony.com/bot/%s" + str(bot_instance_guid), {"message": message})
