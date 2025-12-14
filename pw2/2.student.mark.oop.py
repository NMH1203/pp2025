class Student:
    def __init__(self, sid: int, name: str, dob: str):
        self._id = sid
        self._name = name
        self._dob = dob

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def dob(self):
        return self._dob

    def __str__(self):
        return f"({self._id}, '{self._name}', '{self._dob}')"


class Course:
    def __init__(self, cid: int, name: str):
        self._id = cid
        self._name = name
        self._marks = []

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def add_mark(self, student_name: str, score: float):
        self._marks.append((student_name, score))

    def marks(self):
        return list(self._marks)

    def __str__(self):
        if self._marks:
            return f"({self._id}, '{self._name}', {self._marks})"
        else:
            return f"({self._id}, '{self._name}')"


class MarkManager:
    def __init__(self):
        self._students = []
        self._courses = []

    def input_students(self):
        n = int(input('type in the number of student: '))
        for i in range(1, n + 1):
            sid = int(input(f'ID student {i}: '))
            name = input(f'Name student {i}: ')
            dob = input(f'DoB student {i}: ')
            self._students.append(Student(sid, name, dob))

    def input_courses(self):
        n = int(input('Type in the number course: '))
        for i in range(1, n + 1):
            cid = int(input(f'ID course {i}: '))
            name = input(f'Name course {i}: ')
            self._courses.append(Course(cid, name))

    def find_course(self, cid: int):
        for course in self._courses:
            if course.id == cid:
                return course
        return None

    def input_marks_for_course(self):
        cid = int(input('Type the ID of the course to write mark: '))
        course = self.find_course(cid)
        if not course:
            print(f'Course with ID {cid} not found.')
            return
        for student in self._students:
            score = float(input(f'Type the mark for {student.name}: '))
            course.add_mark(student.name, score)
        print('\nStudent mark list:', course.marks())

    def show_students(self):
        print('\nList of student information:')
        for s in self._students:
            print(f'  {s}')

    def show_courses(self):
        print('\nList of course information:')
        for c in self._courses:
            print(f'  {c}')


def main():
    mm = MarkManager()
    mm.input_students()
    mm.input_courses()
    mm.input_marks_for_course()
    mm.show_students()
    mm.show_courses()


if __name__ == '__main__':
    main()
