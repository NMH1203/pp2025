import os
import zipfile

def load_data():
    if not os.path.exists("students.dat"):
        return [], [] # Trả về list rỗng nếu chưa có file

    # 1. Giải nén
    with zipfile.ZipFile("students.dat", "r") as zipf:
        zipf.extractall() # Bung nén ra thư mục hiện tại

    students = []
    courses = []

    # 2. Đọc file students.txt
    if os.path.exists("students.txt"):
        with open("students.txt", "r", encoding="utf-8") as f:
            for line in f:
                
                parts = line.strip().split("|") 
                if len(parts) == 3:
                    
                    new_student = student(int(parts[0]), parts[1], parts[2])
                    students.append(new_student)
    
    # ... Làm tương tự cho courses.txt và marks.txt ...
    
    return students, courses