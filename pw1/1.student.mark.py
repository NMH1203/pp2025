Number_student = int(input("type in the number of student: "))

Student_information= list()

for i in range(1,Number_student+1):
    id_Student=int(input("ID student " +str(i)+": "))
    Name_student= input ("Name student "+str(i)+": ")
    DoB_Student= input ("DoB student "+str(i)+": ")
    Information=(id_Student, Name_student, DoB_Student)
    Student_information.append(Information)

Course_number= int(input ("Type in the number course: "))

Course_information=list()

for i in range (1,Course_number+1):
    id_course = int(input("ID course "+str(i)+": "))
    Name_course= input("Name course "+str(i)+": ")
    Information=(id_course, Name_course)
    Course_information.append(Information)

Course_Mark=int(input("Type the ID of the course to write mark: "))

Course_index = None

for i in range(len(Course_information)):
    if Course_Mark == Course_information[i][0]:
        Course_index = i
        break

if Course_index is not None:
    marks_list = []
    for j in range(len(Student_information)):
        mark = float(input(f"Type the mark for {Student_information[j][1]}: "))
        Mark_entry = (Student_information[j][1], mark)
        marks_list.append(Mark_entry)
    
    course_data = list(Course_information[Course_index])
    course_data.append(marks_list)
    Course_information[Course_index] = tuple(course_data)
else:
    print(f"Course with ID {Course_Mark} not found.")



print("List of student information: \n", Student_information)
print("List of course information: \n ", Course_information )
print("Student mark list: ", marks_list)