# Module Imports
import mariadb
import sys


# Creating a class for student

class Student():

    def __init__(self, id_number=-1, first_name="", middle_name="", last_name="", age=-1):
        self.id_number = id_number
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.age = age
        self.connection = mariadb.connect(
            user="admin",
            password="majevince",
            host="127.0.0.1",
            port=3306,
            database="test"

        )  # Connect to MariaDB Platform
        self.cursor = self.connection.cursor()  # defining cursor

    def load_student(self, id_number):
        self.cursor.execute("""
        SELECT * FROM students
        WHERE id = {}
        """.format(id_number))

        results = self.cursor.fetchone()
        print(results)
        self.id_number = id_number
        self.first_name = results[1]
        self.middle_name = results[2]
        self.last_name = results[3]


s1 = Student()
s1.load_student(1)
print(f"My Student ID Number:{s1.id_number}")
print(f"My First name is: {s1.first_name}")
print(f"My Last name is: {s1.last_name}")