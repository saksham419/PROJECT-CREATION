# import mysql.connector
# import pandas as pd

# # Connect to MySQL
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Sa@070706",
#     database="healthcare_db"
# )

# # Query data
# query = """
# SELECT d.disease_name, s.symptom_name
# FROM diseases d
# JOIN disease_symptom_relation dsr ON d.disease_id = dsr.disease_id
# JOIN symptoms s ON s.symptom_id = dsr.symptom_id;
# """

# df = pd.read_sql(query, conn)
# conn.close()

# print("Sample Data:")
# print(df.head())

# # Save dataset
# df.to_csv("disease_symptom_dataset.csv", index=False)
# print("✅ Dataset saved as disease_symptom_dataset.csv")

import mysql.connector
import pandas as pd

# ✅ Connect to your database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sa@070706",  # ⚠️ Replace with your actual MySQL password
    database="healthcare_db"
)

# ✅ Query to fetch disease-symptom pairs
query = """
SELECT d.disease_name, s.symptom_name
FROM diseases d
JOIN disease_symptom_relation dsr ON d.disease_id = dsr.disease_id
JOIN symptoms s ON s.symptom_id = dsr.symptom_id;
"""

# ✅ Load data into pandas DataFrame
df = pd.read_sql(query, conn)
conn.close()

# ✅ Show sample data
print("🔹 Sample of fetched data:")
print(df.head(10))

# ✅ Save dataset as CSV
df.to_csv("disease_symptom_dataset.csv", index=False)
print("\n✅ Dataset saved as 'disease_symptom_dataset.csv' successfully!")
