import pandas as pd
import pickle

# ✅ Load your training dataset
df = pd.read_csv("ml_training_data.csv")

# ✅ Extract symptom names (all columns except the last one)
symptom_columns = df.columns[:-1].tolist()

# ✅ Save the symptom list
with open("symptom_list.pkl", "wb") as f:
    pickle.dump(symptom_columns, f)

print(f"✅ Created symptom_list.pkl successfully with {len(symptom_columns)} symptoms:")
print(symptom_columns[:20])  # preview first 20
