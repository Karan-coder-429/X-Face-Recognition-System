import cv2
import face_recognition
import numpy as np
import os
import sqlite3
from datetime import datetime

# -----------------------------
# Database Setup
# -----------------------------
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
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cur.execute('INSERT INTO attendance (name, confidence, timestamp) VALUES (?, ?, ?)',
                (name, confidence, timestamp))
    conn.commit()
    conn.close()
    print(f"[INFO] Attendance marked for {name} ({confidence:.2f}%) at {timestamp}")

# -----------------------------
# Load Known Faces
# -----------------------------
def load_known_faces(folder_path):
    known_encodings = []
    known_names = []

    for file in os.listdir(folder_path):
        if file.endswith(('.jpg', '.jpeg', '.png')):
            img = face_recognition.load_image_file(os.path.join(folder_path, file))
            encoding = face_recognition.face_encodings(img)[0]
            known_encodings.append(encoding)
            known_names.append(os.path.splitext(file)[0])
    return known_encodings, known_names

# -----------------------------
# Face Recognition Function
# -----------------------------
def recognize_faces(known_encodings, known_names):
    cap = cv2.VideoCapture(0)
    print("[INFO] Press 'q' to quit the camera window.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Unable to access camera.")
            break

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_encodings, face_encoding)
            confidence = (1 - np.min(face_distances)) * 100 if len(face_distances) > 0 else 0
            name = "Unknown"

            if True in matches:
                best_match_index = np.argmin(face_distances)
                name = known_names[best_match_index]

            # Draw box
            top, right, bottom, left = [v * 4 for v in (top, right, bottom, left)]
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, f"{name} ({confidence:.1f}%)", (left + 6, bottom - 6),
                        cv2.FONT_HERSHEY_DUPLEX, 0.7, (0, 0, 0), 1)

            if name != "Unknown" and confidence > 70:
                mark_attendance(name, confidence)

        cv2.imshow('Smart Face Recognition - X', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# -----------------------------
# Main Program
# -----------------------------
# if _name_ == "_main_":
#     print("=== Smart Face Recognition System by X ===")
#     print("[INFO] Initializing system...")
#     create_table()

#     known_encodings, known_names = load_known_faces("people/known_faces")
#     if not known_names:
#         print("[WARNING] No known faces found in 'people/known_faces' folder.")
#     else:
#         print(f"[INFO] Loaded {len(known_names)} known faces: {known_names}")

#     recognize_faces(known_encodings, known_names)