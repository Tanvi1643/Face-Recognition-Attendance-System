import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : "https://faceattendancerealtime-ede7f-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "21DIT004":
        {
            "name": "Tanvi Bhatt",
            "Major": "AI & ML",
            "Starting Year": 2021,
            "Total Attendance": 65,
            "Standing": "G",
            "Year": 2,
            "Last Attendance Time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "Major": "Economics",
            "Starting Year": 2018,
            "Total Attendance": 12,
            "Standing": "B",
            "Year": 2,
            "Last Attendance Time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "Major": "Physics",
            "Starting Year": 2020,
            "Total Attendance": 7,
            "Standing": "G",
            "Year": 2,
            "Last Attendance Time": "2022-12-11 00:54:34"
        },
    "21DIT050":
        {
            "name": "Dhruv Patel",
            "Major": "IT",
            "Starting Year": 2020,
            "Total Attendance": 12,
            "Standing": "B",
            "Year": 3,
            "Last Attendance Time": "2022-12-11 00:54:34"
        }
}

for key,value in data.items():
    ref.child(key).set(value)