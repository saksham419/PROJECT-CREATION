# from flask import Flask, request, render_template
# import pandas as pd
# import pickle

# app = Flask(__name__)

# # Load model and dataset
# with open("disease_prediction_model.pkl", "rb") as f:
#     model = pickle.load(f)

# df = pd.read_csv("ml_training_data.csv")
# symptoms = df.columns.tolist()[1:]  # skip 'disease_name'

# @app.route('/')
# def home():
#     return render_template('index.html', symptoms=symptoms)

# @app.route('/predict', methods=['POST'])
# def predict():
#     selected_symptoms = request.form.getlist('symptoms')
#     input_data = [1 if symptom in selected_symptoms else 0 for symptom in symptoms]
#     prediction = model.predict([input_data])[0]
#     return render_template('result.html', disease=prediction)

# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for
import pickle
import pandas as pd

app = Flask(__name__)

# Load model and symptom list if available (optional)
try:
    model = pickle.load(open("disease_prediction_model.pkl","rb"))
    symptom_cols = list(pd.read_csv("ml_training_data.csv").columns)[1:]
except Exception as e:
    model = None
    symptom_cols = ["fever","cough","headache"]  # fallback stub

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', symptoms=symptom_cols, prediction=None, year="2025")

@app.route('/predict', methods=['POST'])
def predict():
    selected = request.form.getlist('symptoms')
    # If model available, predict using symptom order
    if model:
        # build input vector based on symptom_cols
        input_vec = [1 if s in selected else 0 for s in symptom_cols]
        pred = model.predict([input_vec])[0]
    else:
        pred = "No model loaded"

    return render_template('index.html', symptoms=symptom_cols, prediction=pred, year="2025")

# if __name__ == "__main__":
#     app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
