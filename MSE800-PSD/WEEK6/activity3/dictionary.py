
# Dictionary 1
import string


student1 = {
    "name": "Alex",
    "age": 42,
    "course": "Data Analytics",
    "city": "Auckland",
    "status": "Lecturer"
}
 
# Dictionary 2
student2 = {
    "name": "Sophia",
    "age": 29,
    "course": "Software Engineering",
    "city": "Wellington",
    "status": "Student"
}
 
# Dictionary 3
student3 = {
    "name": "Michael",
    "age": 35,
    "course": "Cyber Security",
    "city": "Christchurch",
    "status": "Researcher"
}

# merged_students = [student1, student2, student3]
# result_dic = [student for student in merged_students if student.get("name") == "azw"]
result_dic = {**{k: v for k, v in student1.items() if k == "name" and 'ex' in v}, 
              **{k: v for k, v in student2.items() if k == "name" and 'ex' in v}, 
              **{k: v for k, v in student3.items() if k == "name" and 'ex' in v}}
if not result_dic:
    print("No student found with the name 'Alex'.")
else:
    print(result_dic)