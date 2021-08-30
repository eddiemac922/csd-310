###IMPORTS
from pymongo import MongoClient
import certifi

###MAIN

if __name__ == "__main__":
    url = "mongodb+srv://admin:admin@cluster0.ayo4d.mongodb.net/pytech?retryWrites=true&w=majority"
    client = MongoClient(url, tlsCAFile=certifi.where())
    db = client.pytech
    students = db.students

###TOTAL QUERY
    print("-- DISPLAYING DOCUMENTS FROM STUDENT COLLECTION WITH find() QUERY --\n")
    for s in students.find():
        print(f"\tStudent ID: {s['student_id']}\n\tFirst Name: {s['first_name']}\n\tLast Name: {s['last_name']}\n")

###SINGLE QUERY
    print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --\n")
    s = students.find_one({"student_id": 1007})
    print(f"\tStudent ID: {s['student_id']}\n\tFirst Name: {s['first_name']}\n\tLast Name: {s['last_name']}\n")

    input("\nEnd of program, press any key to exit...\n")

