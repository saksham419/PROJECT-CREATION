import mysql.connector

def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sa@070706",
            database="healthcare_db"
        )
        print("✅ Database connection successful!")
        return connection

    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")
        return None
