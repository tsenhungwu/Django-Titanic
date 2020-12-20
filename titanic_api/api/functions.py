import pickle
import pandas as pd

def load_model(path):
    model = pickle.load(open(path, 'rb'))
    return(model)

def classify_passenger(model, data):
    df = pd.read_json(data)
    pred = model.predict(df)
    return(pred)
