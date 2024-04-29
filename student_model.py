import csv
import os
from datetime import datetime

class Student:
    def __init__(self, id, name, dob, email, phone_number, department, age):
        self._id = id
        self._name = name
        self._dob = dob
        self._email = email
        self._phone_number = phone_number
        self._department = department
        self._age = age

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def dob(self):
        return self._dob

    @property
    def email(self):
        return self._email

    @property
    def phone_number(self):
        return self._phone_number

    @property
    def department(self):
        return self._department

    @property
    def age(self):
        return self._age

class StudentModel:
    FILE_NAME = "students.csv"
    _students_cache = {}

    @classmethod
    def create_student(cls, student):
        cls._ensure_file_exists()
        student._id = cls.generate_id()
        with open(cls.FILE_NAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([student.id, student.name, student.dob, student.email, student.phone_number, student.department, student.age])
        cls._update_cache(student)

    @classmethod
    def read_students(cls):
        if cls._students_cache:
            return list(cls._students_cache.values())
        cls._ensure_file_exists()
        students = []
        with open(cls.FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            header = next(reader, None)  # Read the header row
            if header is None:
                return []  # File is empty, return empty list
            for row in reader:
                student = Student(*row)
                students.append(student)
                cls._update_cache(student)
        return students

    @classmethod
    def update_student(cls, email, new_student_info):
        students = cls.read_students()
        updated = False
        for student in students:
            if student.email == email:
                student._name = new_student_info['name']
                student._dob = new_student_info['dob']
                student._phone_number = new_student_info['phone_number']
                student._department = new_student_info['department']
                student._age = new_student_info['age']
                updated = True
                cls._update_cache(student)
                break
        if updated:
            cls._write_students_to_file(students)
        return updated

    @classmethod
    def delete_student_by_email(cls, email):
        students = cls.read_students()
        deleted = False
        updated_students = []
        for student in students:
            if student.email == email:
                deleted = True
                cls._remove_from_cache(student)
            else:
                updated_students.append(student)
        if deleted:
            cls._write_students_to_file(updated_students)
        print("Deleted successfully!")

    @classmethod
    def delete_all_students(cls):
        cls._students_cache.clear()
        with open(cls.FILE_NAME, mode='w', newline='') as file:
            file.truncate(0)  # Clear file content
        print("Deleted Successfully!")

    @classmethod
    def generate_id(cls):
        students = cls.read_students()
        if not students:
            return 1
        else:
            return int(students[-1].id) + 1

    @classmethod
    def _ensure_file_exists(cls):
        if not os.path.exists(cls.FILE_NAME):
            with open(cls.FILE_NAME, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Id', 'Name', 'DOB', 'Email', 'Phone Number', 'Department', 'Age'])  # Header

    @classmethod
    def _write_students_to_file(cls, students):
        with open(cls.FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Id', 'Name', 'DOB', 'Email', 'Phone Number', 'Department', 'Age'])  # Write header
            for student in students:
                writer.writerow([student.id, student.name, student.dob, student.email, student.phone_number, student.department, student.age])

    @classmethod
    def _update_cache(cls, student):
        cls._students_cache[student.email] = student

    @classmethod
    def _remove_from_cache(cls, student):
        if student.email in cls._students_cache:
            del cls._students_cache[student.email]
