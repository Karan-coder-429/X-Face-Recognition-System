import sqlite3
from datetime import datetime

def create_table():
    conn = sqlite3.connect('attendance.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            confidence REAL,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def mark_attendance(name, confidence):
    conn = sqlite3.connect('attendance.db')
    cur = conn.cursor()
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cur.execute('INSERT INTO attendance (name, confidence, timestamp) VALUES (?, ?, ?)', 
                (name, confidence, time))
    conn.commit()
    conn.close()