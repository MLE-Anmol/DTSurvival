import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('clf.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


def convert_to_str(int):
    word_dict = {1: 'Survived', 0: 'Not Survived'}
    return word_dict[int]


@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = convert_to_str(prediction[0])

    return render_template('index.html', prediction_text='sailor has {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)