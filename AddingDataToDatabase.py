import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("faceattecdance-firebase-adminsdk-612fh-098fa719ad.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://faceattecdance-default-rtdb.firebaseio.com/'
})

ref = db.reference('Students')

data = {
    '001':
        {
            'name': 'Bill Gates',
            'major': 'CSE',
            'standing': 'O',
            'year' : '4th',
            'starting_year ': '2022',
            'total_attendance': 11,
            'last_attendance_time': '2024-10-01 10:29:03'
    },
    '002':
        {
            'name': 'Elon Musk',
            'major': 'CSE',
            'standing': 'O',
            'year' : '4th',
            'starting_year ': '2022',
            'total_attendance': 11,
            'last_attendance_time': '2024-10-01 10:29:03'
    },
    '003':
        {
            'name': 'Steve Jobs',
            'major': 'CSE',
            'standing': 'O',
            'year' : '4th',
            'starting_year ': '2022',
            'total_attendance': 11,
            'last_attendance_time': '2024-10-01 10:29:03'
    }
}

for key,value in data.items():
    ref.child(key).set(value)
