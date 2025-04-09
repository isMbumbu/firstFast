from fastapi import FastAPI , Path
from typing import Union, Optional
from pydantic import BaseModel
app=FastAPI()

students={
    1: {
        "name":"John",
        "age":17,
        "class":"Form 1 Red"
    },
    2: {
        "name":"Drew",
        "age":13,
        "year":"Form 2 Blue"
    }

}

class Student(BaseModel):
    name: str
    age: int
    year: str

@app.get("/")
def home():
    return {"name":"first Data"}

@app.get("/all_students")
def all_students():
    return students

@app.get("/get_students/{student_id}")
def get_students(student_id: int=Path(..., description="The ID of the student", gt=0)):
    return students[student_id]


@app.get("/get_student_by_name")
def get_student_by_name(student_name: str):
    for student_id in students:
        if students[student_id]["name"] == student_name:
            return students[student_id]
    return {"Data": "not found"}  

@app.post("/create_student/{student_id}")
def create_student(student_id : int, student: Student):
    if student_id in students:
        return {"Error":"ID exists already"}
    students[student_id]= Student
    return students[student_id]
     