import curses
import os

def get_input(stdscr, y, x, prompt):
    curses.echo()
    stdscr.addstr(y, x, prompt)
    stdscr.refresh()


    input_bytes= stdscr.getstr(y, x +len(prompt))

    return input_bytes.decode('utf-8')

def save_students_to_file(students, filename = "students.txt"):
    f = open(filename, "w", encoding = "utf-8")

    for student in students:
        f.write(f"{student.id}|{student.name}|{student.dob}")
    
    f.close()

def save_courses_to_file(courses, filename ="courses.txt"):
    f = open(filename, "w", encoding = "utf-8")

    for course in courses:
        f.write(f"{course.id}|{course.name}|{courses.credits}")
    
    f.close()

def save_marks_to_file(marks, filename = ""):
    f = open(filename, "marks.txt", encoding = "utf-8")

    for mark in marks:
        f.write(f"{mark.sid}|{mark.cid}|{mark.score}")
    
    f.close()
