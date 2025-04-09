from fastapi import FastAPI , Path
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
        "class":"Form 2 Blue"
    }

}

@app.get("/")
def home():
    return {"name":"first Data"}

@app.get("/all_students")
def all_students():
    return students

@app.get("/get_students/{student_id}")
def get_students(student_id: int=Path(None, description="The ID of the student")):
    return students[student_id]