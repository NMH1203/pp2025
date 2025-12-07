import math 
import numpy as np

class Student:
    def __init__(self, sid: int , name: str, dod: str):
        self._id = sid
        self._name= name
        self._dod= dod
        self._mark= []
    
    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @property
    def dod(self):
        return self._dod
    
    @property
    def mark(self):
        return self._mark
    
    def add_mark(self, course: str, score: int, credits):
        self._mark.append((course, score, credits))
    
    def __str__(self):
        if self._mark:
            return f"({self._id}. '{self._name}', '{self._dod}', '{self._mark}')"
        else: 
            return f"({self._id}. '{self._name}', '{self._dod}')"
        
    

class Course:
    def __init__(self, cid: int, name: str, credit: int):
        self._id=cid
        self._name= name
        self._mark = []
        self._credits = credit
    
    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name
    
    @property
    def credit(self):
        return self._credits 

    def add_mark(self, student_name: str, score: str, credit: int):
        self._mark.append((student_name, score, credit))
    
    def mark(self):
        return self._mark
    
    def __str__(self):
        if self._mark:
            return f"({self._id}, '{self._name}', {self._mark})"
        else:
            return f"({self._id}, '{self._name}')"

class Markmanager:
    def __init__(self):
        self._student= []
        self._courses= []

    def input_student(self):
        n= int(input("Type in the number of student: "))
        for i in range (1, n+1):
            sid= int(input(f'ID student {i}'))
            name=input (f'Name student {i}') 
            dob= input(f'Dob student {i}')
            self._student.append(Student(sid, name, dob))

    def input_courses(self):
        n = int(input('Type in the number course: '))
        for i in range(1, n + 1):
            cid = int(input(f'ID course {i}: '))
            name = input(f'Name course {i}: ')
            credit=int(input(f'Credit of course {i}: '))
            self._courses.append(Course(cid, name, credit))

    def find_course(self, id:int):
        for course in self._courses:
            if(course.id == id):
                return course
        return None
    
    def input_marks_for_course(self):
        cid = int(input("Type the id of the course to write mark: "))
        course = self.find_course(cid)
        if not course:
            print(f'course with id {cid} not found')
            return 
        for student in self._student:
            score = math.floor(float(input(f'Type the mark for {student.name}: ')))
            course.add_mark(student.name, score)
            student.add_mark(course.name, score, course.credit)
        print('\nStudent mark list:',course.mark())

    def find_student(self,id:int):
        for astudent in self._student:
            if(id==astudent.id):
                return astudent
        return None

    def calculate_GPA(self):
        sID=int(input("write the ID of student you want to calculate GPA: "))
        student=self.find_student(sID)
        if student is None:
            print(f"student with ID {sID} not found")
            return
        scores=[score for [_course, score, credit] in student.mark]
        credits=[credit for [_course, score, credit] in student.mark]
        if not scores:
            print("no mark available for this student")
            return
        np_scores=np.array(scores)
        np_credits=np.array(credits)
        gpa = float(np.average(np_scores,weights= np_credits))
        print(f"Student {student.name} (ID {student.id}) GPA: {gpa:.2f}")

    def show_student(self):
            print('\n Student information: ')
            for s in self._student:
                print(f' {s}')
    
    def show_course(self):
        print('\nList of course information: ')
        for c in self._courses:
            print(f' {c}')

    def help(self):
        print("--help--")
        print("1: input student")
        print("2 input course")
        print("3 input input mark of the course")
        print("4: show students")
        print("5: show courses")
        print("6: calculate student GPA ")
        print("7: help")
        print("8: exit")


def main():
    mm = Markmanager()
    mm.input_student()
    mm.input_courses()

    while True:
        mode= input("enter the action: ")
        match mode:
            case "1":
                mm.input_student()
            case "2":
                mm.input_courses()
            case "3":
                mm.input_marks_for_course()
            case "4":
                mm.show_student()
            case "5":
                mm.show_course()
            case "6" :
                mm.calculate_GPA()
            case "7" | "help":
                mm.help()
            case "8":
                break
            case _:
                print("invalid action")

if __name__ == '__main__':
    main()

    
