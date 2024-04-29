import re
from datetime import datetime
from student_model import StudentModel, Student
from student_view import StudentView

class StudentController:
    @staticmethod
    def create_student():
        name, dob, email, phone_number, department, age = StudentView.get_student_info()
        student = Student(None, name, dob, email, phone_number, department, age)
        StudentModel.create_student(student)
        print("Student created successfully!")

    @staticmethod
    def read_students():
        students = StudentModel.read_students()
        StudentView.display_students(students)

    @staticmethod
    def update_student():
        email = input("Enter email of the student to update: ")
        new_student_info = StudentView.get_student_info_for_update(email)
        if new_student_info is not None:  # Check if new_student_info is not None
            if StudentModel.update_student(email, new_student_info):
                print("Updated Successfully!")
            else:
                 print("Not Yet Updated! There are some Problems!")


    @staticmethod
    def delete_student():
        choice = input("Do you want to delete by email (E) or delete all (A)? (E/A): ").upper()
        if choice == 'E':
            email = input("Enter email of the student to delete: ")
            StudentModel.delete_student_by_email(email)
        elif choice == 'A':
            StudentModel.delete_all_students()
        else:
            print("Invalid choice. Please enter 'E' or 'A'.")

    @staticmethod
    def view_student_by_email():
        email = input("Enter email of the student to view: ")
        students = StudentModel.read_students()
        StudentView.display_students_by_email(email, students)
