###IMPORTS

from pymongo import MongoClient
import certifi

###MAIN

if __name__ == "__main__":
    url = "mongodb+srv://admin:admin@cluster0.ayo4d.mongodb.net/pytech?retryWrites=true&w=majority"
    client = MongoClient(url, tlsCAFile=certifi.where())
    db = client.pytech
    studentColl = db.students

###STUDENTS
    
students = [{"student_id": 1007,"first_name" : "Mike", "last_name" : "Jones"},
            {"student_id": 1008,"first_name" : "Eddie", "last_name" : "Kain"},
            {"student_id": 1009,"first_name" : "Timmy", "last_name" : "Turner"}]
###INSERTS

print("-- INSERT STATEMENTS --")
for student in students:
    Object_id = studentColl.insert_one(student)
    print(f"Inserted student {student['first_name']} {student['last_name']} into the students collections with document id {Object_id.inserted_id}.")

input("\nEnd of program, press any key to exit... ")

