

import sqlite3


class Student:

    def __init__(self, StudentID, FirstName, LastName, GPA, Major, FacultyAdvisor):

        self.StudentID = StudentID
        self.FirstName = FirstName
        self.LastName = LastName
        self.GPA = GPA
        self.Major = Major
        self.FacultyAdvisor = FacultyAdvisor

