from certifai.model.sdk import SimpleModelWrapper
import pickle

with open('german_credit_mlp.pkl', 'rb') as f:
    saved = pickle.load(f)
    model = saved.get('model')
    encoder = saved.get('encoder', None)

# to enable models with soft-scores use `supports_soft_scores=True` when initializing SimpleModelWrapper
# scikit mlp classifier provides default implementation for soft_scores using `predict_proba` method
# in-order to provide own soft scoring method override SimpleModelWrapper.soft_predict
# optionally, add ordered list of score_labels. default labels are derived using `model._classes` provided by scikit mlp
# these are ordered wrt to model predict scores. e.g. if score_labels = [1,2] then scores of [0.3,0.7] -> [1,2] labels
# follow certifai.model.sdk docs for more info.
# https://cognitivescale.github.io/cortex-certifai/certifai-api-ref-1.3.5/certifai.model.html

app = SimpleModelWrapper(supports_soft_scores=True, model=model, encoder=encoder, score_labels=[1, 2],
                         endpoint_url='/german_credit_mlp/predict')

# to start production ready gunicorn server use `production=True`
app.run(production=True)
