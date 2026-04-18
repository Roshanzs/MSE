
students = []

class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

def collect_info():
    for i in range(3):
        student_str = f"Student {i + 1}"
        name = input(f"Enter the name of {student_str}: ")
        age = int(input(f"Enter the age of {student_str}: "))
        student_id = i + 1
        student = Student(name, age, student_id)
        students.append(student)

def display_students():
    for student in students:
        sorted_students = sorted(students, key=lambda s: s.name)
    for student in sorted_students:
        student.display_info()

if __name__ == "__main__":
    collect_info()
    display_students()