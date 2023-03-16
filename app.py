from fastapi import FastAPI, Path

app = FastAPI()

students = {
  1: {
    "name": "John Smith",
    "class": "5A",
    "age": 10
  },
  2: {
    "name": "Jane Doe",
    "class": "6B",
    "age": 11
  },
  3: {
    "name": "Bob Johnson",
    "class": "4C",
    "age": 9
  }
}


@app.get("/")
def index():
    return {"welcome": "first Page"}


@app.get("/get_student/{student_id}")
def index(student_id: int = Path(None, description="The id of student", gt=0, lt=4)):
    return students[student_id]