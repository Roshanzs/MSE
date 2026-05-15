from decorators import log_activity


#add the decorator to the student_login function to implement commonly used code in the log_activity function
@log_activity
#implement the student_login function to print the username of the student who logged in
def student_login(username):
    print(f"{username} logged into the system.")

#add the decorator to the submit_assignment function to implement commonly used code in the log_activity function
@log_activity
#implement the submit_assignment function to print the username of the student who submitted the assignment and the name of the assignment
def submit_assignment(username, assignment):
    print(f"{username} submitted {assignment}.")

#add the decorator to the view_grades function to implement commonly used code in the log_activity function
@log_activity
#implement the view_grades function to print the username of the student who is viewing grades
def view_grades(username):
    print(f"{username} is viewing grades.")
