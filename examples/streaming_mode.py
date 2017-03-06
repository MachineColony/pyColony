from sklearn import datasets
from mc import MC


mc = MC({'user': {'client_key': '',
                  'client_secret': ''}})

categories = ['alt.atheism', 'talk.religion.misc']

ds_train = datasets.fetch_20newsgroups(subset='train', categories=categories)
ds_test = datasets.fetch_20newsgroups(subset='test', categories=categories)


def create_model():
    r = mc.create_bayes_classifier({'data': {'x': ds_train.data, 'y': ds_train.target.tolist()},
                                    'params': {'alpha': 0.01}})
    return r['data']['model_id']


def evaluate(model_id):
    stream = mc.evaluate_model_streaming(model_id, 'bayes')
    for x, y in zip(ds_test.data, ds_test.target):
        r = stream.predict([x])
        print 'predict:', r, 'actual:', y
    stream.close()

