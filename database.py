import sqlite3

def init_db():
    conn = sqlite3.connect('health_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS health_records (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id TEXT,
                        symptoms TEXT,
                        chronic_issues TEXT,
                        advice TEXT)''')
    conn.commit()
    conn.close()

def save_user_data(data):
    conn = sqlite3.connect('health_data.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO health_records (user_id, symptoms, chronic_issues, advice) VALUES (?, ?, ?, ?)", 
                   (data['user_id'], data['symptoms'], data['chronic_issues'], data['advice']))
    conn.commit()
    conn.close()

def fetch_user_data(user_id):
    conn = sqlite3.connect('health_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM health_records WHERE user_id = ?", (user_id,))
    data = cursor.fetchall()
    conn.close()
    return data

# Initialize the database
init_db()