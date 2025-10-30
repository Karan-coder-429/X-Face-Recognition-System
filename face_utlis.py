import face_recognition
import cv2
import os
import numpy as np

def load_known_faces(known_dir="people/known_faces"):
    known_encodings = []
    known_names = []

    for filename in os.listdir(known_dir):
        if filename.lower().endswith(('.jpg', '.png', '.jpeg')):
            path = os.path.join(known_dir, filename)
            img = face_recognition.load_image_file(path)
            encs = face_recognition.face_encodings(img)
            if encs:
                known_encodings.append(encs[0])
                known_names.append(os.path.splitext(filename)[0])
    return known_encodings, known_names


def recognize_face(frame, known_encodings, known_names, tolerance=0.5):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    results = []
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance)
        face_distances = face_recognition.face_distance(known_encodings, face_encoding)
        name = "Unknown"
        confidence = 0.0

        if True in matches:
            best_match_index = np.argmin(face_distances)
            name = known_names[best_match_index]
            confidence = (1 - face_distances[best_match_index]) * 100

        results.append((name, confidence, (top, right, bottom, left)))
    return results