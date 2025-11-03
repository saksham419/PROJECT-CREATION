from db_connection import connect_db

def get_diseases_by_symptoms(symptoms_list):
    """Fetch possible diseases based on multiple symptoms."""
    conn = connect_db()
    if not conn:
        print("❌ Database connection failed.")
        return []

    cursor = conn.cursor()

    placeholders = ', '.join(['%s'] * len(symptoms_list))
    query = f"""
        SELECT 
            d.disease_name,
            ANY_VALUE(d.description) AS description,
            ANY_VALUE(d.treatment) AS treatment,
            COUNT(*) AS match_count
        FROM diseases d
        JOIN disease_symptom_relation dsr ON d.disease_id = dsr.disease_id
        JOIN symptoms s ON dsr.symptom_id = s.symptom_id
        WHERE s.symptom_name IN ({placeholders})
        GROUP BY d.disease_name
        ORDER BY match_count DESC;
    """

    cursor.execute(query, tuple(symptoms_list))
    results = cursor.fetchall()
    conn.close()
    return results

def main():
    print("\n🩺 Welcome to the Healthcare Symptom Checker 🩺")
    print("Enter your symptoms separated by commas (e.g., fever, cough, headache)")
    
    # Get multiple symptoms as a list
    user_input = input("\nEnter symptoms: ").strip().lower()
    symptoms_list = [sym.strip().title() for sym in user_input.split(",") if sym.strip()]

    if not symptoms_list:
        print("⚠️ Please enter at least one symptom.")
        return

    diseases = get_diseases_by_symptoms(symptoms_list)

    if diseases:
        print("\n✅ Based on your symptoms, possible diseases are:\n")
        for name, desc, treat, match in diseases:
            print(f"🦠 Disease: {name}")
            print(f"   • Description: {desc}")
            print(f"   • Treatment: {treat}")
            print(f"   • Symptom Match Count: {match}")
            print("--------------------------------------------------")
    else:
        print("\n❌ No diseases found for the given symptoms. Try different ones.")

if __name__ == "__main__":
    main()
