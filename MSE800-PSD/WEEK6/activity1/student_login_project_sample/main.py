from users import (
    student_login,
    submit_assignment,
    view_grades
)


def main():
    #implement the function to call the student_login functions
    student_login("Mohammad")
    #implement the submit_assignment function 
    submit_assignment(
        "Mohammad",
        "Python Decorator Project"
    )
    #implement the view_grades function 
    view_grades("Alex")


if __name__ == "__main__":
    main()
