import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("serviceAccountKey.json")
#firebase_admin.initialize_app(cred)

firebase_admin.initialize_app(cred,

{
    'databaseURL': "https://face-recognition-real-ti-fb2f9-default-rtdb.firebaseio.com/"
})



ref = db.reference('People')

data = {
    "321654":
        {
            "name": "Nour Zayed",
            "major": "AL || Data Analyst",
            "starting_year": 2024,
            "total_attendance": 5,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2024-12-11 00:54:34"
        },


        
    "852741":
        {
            "name": "Magdy  Yacoub ",
            "major": "Cardiologist",
            "starting_year": 1962,
            "total_attendance": 10,
            "standing": "B",
            "year": +60,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }

        ,
        "123456":
        {
            "name": "Andrew ng",
            "major" :" Founder of DeepLearning.AI",
            "starting_year":2000,  
            "total_attendance": 7,
            "standing": "G",
            "year": +50,
            "last_attendance_time": "2022-12-11 00:54:34"
        }

}
for key, value in data.items():
    ref.child(key).set(value)
    
    
