# X-Face-Recognition-System
Here is the Face Recognition System which is developed by X pvt Ltd you can take samrt ai powered attendance

# 🧠 Smart Face Recognition System by X (Console Prototype)

### 👨‍💻 Developer: Khasor Karan  
*Enrollment No:* 160110524061  
*Organization:* X — Independent AI R&D Initiative  

---

## 📘 Overview
The *Smart Face Recognition System* is a console-based prototype that automatically detects and recognizes human faces using AI.  
It marks attendance securely in a local SQLite database.  
This is the *base version, and an advanced **FastAPI-powered web dashboard* is currently *under development*.

---

## ⚙ Tech Stack
- *Python 3.9+*
- *OpenCV* – for camera & image processing  
- *face_recognition (dlib)* – for face encoding and matching  
- *NumPy, Pandas* – for data handling  
- *SQLite3* – for attendance storage  

---

## 📁 Project Structure

---

## ▶ How to Run
```bash
# 1. Create virtual environment (optional)
python -m venv venv
venv\Scripts\activate        # On Windows
# source venv/bin/activate   # On Linux/Mac

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the system
python main.py

# __________________________________________________________________________________________________________________________________________

Once Started,the webcam will open automatically
press 'q' to close the camera window anytime

___________________________________________________________________________________________________________________________________________

Database Info -

Attendance is saved in attendance.db in the following formate

ID   Name      Confidence  Timestamp

1 khasorkaran  95.2       2025-10-30
2 DivyaKhandesi 91.7      2025-10-30

________________________________________________________________________________________________________________________________________

Future Development

- FastAPI Backend For Remote Atendance
- Web Dashboard FOr Live Monitoring
- Anti-spoofing Deep Learning Model
- Multi - Camera Support For Institutions

_________________________________________________________________________________________________________________________________________

Status -

- Console Version Completed
- FastAPI Version - Under Development
__________________________________________________________________________________________________________________________________________

Contact -

Khasor Karan
Email - khasorkaran1@gmail.com
B.Tech CTIS Stduent,ITM Vocational University
Project By X (indepedant AI & DeepLearning R&D Initative)


