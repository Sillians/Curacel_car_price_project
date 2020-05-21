from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import joblib
import pickle
# from sklearn.externals import joblib


app = Flask(__name__)

model = pickle.load(open("models/model.pkl", 'rb'))
print('Loaded')

features = pickle.load(open("features/featuresdata/features.pkl", 'rb'))
print('Features loaded')


@app.route('/predict', methods = ['POST'])
def predict():

    if request.method == 'POST':

        json_data = request.json
        df = pd.DataFrame(json_data)
        df = pd.get_dummies(df)
        
        df_ = df.reindex(columns = features, fill_value = 0)

        pred = list(model.predict(df_))

        return jsonify({'prediction': str(pred)})

if __name__ == '__main__':
    app.run(debug=True, port = 2000)