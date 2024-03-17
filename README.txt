COMP 3005
Assignment 3 - Question 1
Samantha Beilman
101198530

        Thank you for your time.

Important Notes:
    • If you need to test my submission, please change the constants for database name, username and password in a3q1.py to match your system

Included Files:
    a3q1.py             - the application code
    a3q1-setup.sql      - file which will set up the database to be used by the application
    this README file

Design Decisions:
    • I decided to use psycopg3 because I want to do the first project option, so I wanted to get some experience now. 
    • The connection function required a password on my system, so I added that field. 
        • Either change the password if needed, or remove that field if you don't have a password on.
    • Decided to connect within each function so that each one would be entirely self-sufficient and I wouldn't need to worry about the scope of cur and conn. 


Resources:
    Started from this code sample in the psycopg documentation:
        • https://www.psycopg.org/psycopg3/docs/basic/usage.html#shortcuts