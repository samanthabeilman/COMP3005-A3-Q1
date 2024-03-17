# Note: the module name is psycopg, not psycopg3
import psycopg
import datetime

from a3q1 import DB_NAME
from a3q1 import USER_NAME

from a3q1 import getAllStudents
from a3q1 import addStudent
from a3q1 import updateStudentEmail
from a3q1 import deleteStudent

# controller for the user
def main():
    while(1):
        menu_choice = input("Enter your choice and hit Enter:\n\t0: Get All Students\n\t1: addStudent\n\t2: Update a Student's Email\n\t3: Delete a Student \n")
        try:
            menu_choice = int(menu_choice)
        except:
            print("\n\t\tGOODBYE\n")
            break

        match menu_choice:
            
            case 0: 
                getAllStudents()

            case 1:
                first_name = input("Enter their first name: ")
                last_name = input("Enter their last name: ")
                email = input("Enter their email: ")
                enrollment_day = int(input("Enter their enrollment day: "))
                enrollment_month = int(input("Enter their enrollment month: "))
                enrollment_year = int(input("Enter their enrollment year: "))
                enrollment_date = datetime.date(enrollment_year, enrollment_month, enrollment_day)
                addStudent(first_name, last_name, email, enrollment_date)

            case 2:
                student_id = input("Enter the student id number of the student whose email you would like to change: ")
                new_email = input("Enter the new email for this student: ")
                updateStudentEmail(student_id, new_email)

            case 3:
                student_id = input("Enter the student id number of the student who you would like to delete: \n")
                deleteStudent(student_id)

            case _:
                print("\n\t\tGOODBYE\n")
                break



if __name__ == "__main__":
    main()