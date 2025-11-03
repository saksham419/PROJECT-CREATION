# import pickle
# import pandas as pd

# # Load model and dataset structure
# model = pickle.load(open("symptom_checker_model.pkl", "rb"))
# df = pd.read_csv("ml_training_data.csv")

# symptoms = sorted(df.columns[1:])  # skip 'disease_name'

# # User input
# user_symptoms = input("Enter your symptoms (comma-separated): ").lower().split(',')

# # Prepare input vector
# input_data = [1 if symptom.strip() in user_symptoms else 0 for symptom in symptoms]
# input_df = pd.DataFrame([input_data], columns=symptoms)

# # Predict
# prediction = model.predict(input_df)[0]
# disease_name = df['disease_name'].unique()[prediction]
# print(f"\n🤖 Based on your symptoms, you may have: {disease_name}")


import pandas as pd
import pickle

# Load model
with open("disease_prediction_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load dataset to get symptom columns
df = pd.read_csv("ml_training_data.csv")
symptoms = df.columns.tolist()[1:]  # skip 'disease_name'

def predict_disease(user_symptoms):
    input_data = [1 if symptom in user_symptoms else 0 for symptom in symptoms]
    prediction = model.predict([input_data])[0]
    return prediction

# Example usage
if __name__ == "__main__":
    user_input = ['fever', 'headache', 'body_ache', 'fatigue']
    result = predict_disease(user_input)
    print(f"🩺 Predicted Disease: {result}")
