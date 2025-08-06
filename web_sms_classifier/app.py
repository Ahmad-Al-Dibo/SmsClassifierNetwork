from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
import pickle
from keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

sen_length = 100  
training_historyFile = "data/training_history.json"
tokenizer_file = "data/tokenizer.pkl"
model_path = "Model/lstm_model_1.h5"
model = tf.keras.models.load_model(model_path)

with open(tokenizer_file, 'rb') as f:
    tokenizer = pickle.load(f)


int2word = {0: "ham", 1: "spam"}

def prediction(model, sms):
    seq = tokenizer.texts_to_sequences([sms])
    seq = pad_sequences(seq, maxlen=sen_length)
    predict = model.predict(seq)[0]
    return [int2word[np.argmax(predict)], predict]

@app.route("/", methods=["GET", "POST"])
def index():
    predict_word= None
    predict_values = None
    if request.method == "POST":
        sms = request.form.get("message")
        result = prediction(model, sms)
        [predict_word, predict_values] = result
    return render_template("index.html", result=predict_word, predict_result= predict_values)

@app.route("/metrics")
def metrics():
    import json
    import os
    history = {}
    if os.path.exists(training_historyFile):
        with open(training_historyFile, "r") as f:
            try:
                history = json.load(f)
            except json.JSONDecodeError:
                history = {}
    return render_template("metrics.html", history=history)

if __name__ == "__main__":
    app.run(debug=True)
