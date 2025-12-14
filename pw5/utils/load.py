import os
import zipfile
import tempfile

from domain.models import Student 
from domain.models import Course

def load_data():

    students = []
    courses = []
    marks = []

    if not os.path.exists("students.dat"):
        return students, courses, marks

    with tempfile.TemporaryDirectory() as temp_dir:

        with zipfile.ZipFile("student.dat", "r") as zipf:
            zipf.extractall(temp_dir)

        student_file = os.path.join(temp_dir, "students.txt")

        if os.path.exists(student_file):
            with open(student_file, "r", encoding="utf-8") as f:
                
                for line in f:    
                    parts = line.strip().split("|") 
                    if len(parts) == 3:
                        new_student = Student(int(parts[0]), parts[1], parts[2])
                        students.append(new_student)
        
        course_file = os.path.join(temp_dir, "courses.txt")

        if os.path.exists(course_file):
            with open(course_file, "r", encoding="utf-8") as f :
                
                for line in f:
                    parts = line.strip().split("|")
                    if len(parts) == 3:
                        new_course = Course(int(parts[0]), parts[1], int(parts[2]))
                        courses.append(new_course)

        mark_file= os.path.join(temp_dir, "marks.txt")

        if os.path.exists(mark_file):
            with open(mark_file, "r", encoding = "utf - 8" ) as f:

                for line in f:
                    parts = line.strip().split("|")
                    if len(parts) ==3:
                        marks.append({ int(parts[0]), int(parts[1]), float(parts[2])}) 

        mark_file = os.path.join(temp_dir, "marks.txt")

    return students, courses