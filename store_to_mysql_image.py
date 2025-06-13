import json
import mysql.connector

def main(json_file_path="structured_data.json"):
    try:
        with open(json_file_path, "r") as json_file:
            patient_record = json.load(json_file)
    except FileNotFoundError:
        print(f"Error: JSON file '{json_file_path}' not found.")
        return

    # Update with your credentials
    db_config = {
        "host": "localhost",
        "user": "your_user",  # <-- CHANGE THIS
        "password": "your_password",  # <-- CHANGE THIS
        "database": "hospital_db"
    }

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS patients (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                dob DATE
            );
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS forms_data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                patient_id INT,
                form_json JSON,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (patient_id) REFERENCES patients(id)
            );
        ''')

        name = patient_record.get("patient_name", "Unknown")
        dob = patient_record.get("dob", "2000-01-01")

        cursor.execute("INSERT INTO patients (name, dob) VALUES (%s, %s)", (name, dob))
        patient_id = cursor.lastrowid

        cursor.execute("INSERT INTO forms_data (patient_id, form_json) VALUES (%s, %s)",
                       (patient_id, json.dumps(patient_record)))

        conn.commit()
        print("Data successfully inserted into MySQL database!")

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    main()
