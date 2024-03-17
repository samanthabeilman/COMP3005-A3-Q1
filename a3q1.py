# Note: the module name is psycopg, not psycopg3
import psycopg

DB_NAME = "University2" # TA, please change this if needed for testing!
USER_NAME = "postgres"  # TA, please change this if needed for testing!
PASSWORD = "Apollo8!!"  # TA, please change this if needed for testing!
# ! NOTE remember to take your password out

# Retrieves and displays all records from the students table.
def getAllStudents():
    with psycopg.connect(f"dbname={DB_NAME} user={USER_NAME} password={PASSWORD}") as conn:

        # Open a cursor to perform database operations
        with conn.cursor() as cur:

            # Query the database and obtain data as Python objects.
            cur.execute("SELECT * FROM students;")

            # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
            # of several records, or even iterate on the cursor•
            print("\n------------ Displaying all student records -------------")
            for record in cur:
                print(record)
            print("---------------------------------------------------------\n")
            # Make the changes to the database persistent
            conn.commit()

# Adds a student to the database
            #      first_name: string
            #       last_name: string
            #           email: string
            # enrollment_date: datetime.date(y, m, d)
def addStudent(first_name, last_name, email, enrollment_date):
    with psycopg.connect(f"dbname={DB_NAME} user={USER_NAME} password={PASSWORD}") as conn:

        # Open a cursor to perform database operations
        with conn.cursor() as cur:

            cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);", ( first_name, last_name, email, enrollment_date ))
            # Make the changes to the database persistent
            conn.commit()

# Changes the student with the specified number's email
def updateStudentEmail(student_id, new_email):
    with psycopg.connect(f"dbname={DB_NAME} user={USER_NAME} password={PASSWORD}") as conn:

        # Open a cursor to perform database operations
        with conn.cursor() as cur:

            cur.execute("UPDATE students SET email = (%s) WHERE student_id = (%s);", (new_email, student_id))
            # Make the changes to the database persistent
            conn.commit()

# deletes student with matching ID number
def deleteStudent(student_id):
    with psycopg.connect(f"dbname={DB_NAME} user={USER_NAME} password={PASSWORD}") as conn:

        # Open a cursor to perform database operations
        with conn.cursor() as cur:

            cur.execute("DELETE FROM students WHERE student_id = (%s);", [student_id])
            # Make the changes to the database persistent
            conn.commit()