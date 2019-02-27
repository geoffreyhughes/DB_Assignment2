
import sqlite3
from Student import Student

conn = sqlite3.connect('/Users/geoffrey/Library/Preferences/DataGrip2018.3/projects/Assignment2/StudentDB.db')
c = conn.cursor() #allows python code to execute SQL statements


def create_table():
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS Students (
                  StudentID INTEGER PRIMARY KEY,
                  FirstName varchar(25),
                  LastName varchar(25),
                  GPA NUMERIC,
                  Major varchar(10),
                  FacultyAdvisor varchar(25)
                  )""")
    conn.commit()



def add_student(id, fn, ln, gpa, major, fa):
    c = conn.cursor()
    c.execute("INSERT INTO Students VALUES (?, ?, ?, ?, ?, ?)", (id, fn, ln, gpa, major, fa))
    conn.commit()


def list_all():
    c = conn.cursor()
    c.execute("SELECT * FROM Students")
    print(c.fetchall())


def update_student(update_studentID, update_major, update_fa):
    c = conn.cursor()
    c.execute('''UPDATE Students SET Major = ? WHERE StudentID = ?''',
              (update_major, update_studentID))
    c.execute('''UPDATE Students SET FacultyAdvisor = ? WHERE StudentID = ?''',
              (update_fa, update_studentID))
    conn.commit()


def delete_student(delete_studentID):
    c = conn.cursor()
    c.execute('''DELETE FROM Students WHERE StudentID = ?''',
              (delete_studentID,))
    conn.commit()


def search_by(option):
    c = conn.cursor()

    if option == 1:
        c.execute("SELECT * FROM Students ORDER BY Major")

    if option == 2:
        c.execute("SELECT * FROM Students ORDER BY GPA")

    if option == 3:
        c.execute("SELECT * FROM Students ORDER BY FacultyAdvisor")

    print(c.fetchall())