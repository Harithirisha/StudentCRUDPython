import re
from datetime import datetime
from tabulate import tabulate # type: ignore
from student_model import StudentModel

class StudentView:
    @classmethod
    def get_student_info(cls):
        name = input("Enter student name (max 50 characters, format: Firstname Lastname): ")
        while not re.match("^[A-Za-z ]{1,50}$", name):
            print("Invalid name format or length. Please enter a valid name (max 50 characters, format: Firstname Lastname).")
            name = input("Enter student name again: ")

        dob = input("Enter date of birth (format: YYYY-MM-DD): ")
        while not cls.validate_dob(dob):
            print("Invalid date of birth. You must be older than 18 to register.")
            dob = input("Enter date of birth again (format: YYYY-MM-DD): ")

        age = cls.calculate_age(dob)

        email = input("Enter email (must end with @gmail.com): ")
        while not cls.validate_email(email):
            print("Invalid email format or already exists. Please enter a valid email.")
            email = input("Enter email again: ")

        phone_number = input("Enter phone number (10 digits): ")
        while not cls.validate_phone_number(phone_number):
            print("Invalid phone number. Please enter a 10-digit phone number.")
            phone_number = input("Enter phone number again: ")

        department = input("Enter department (CSE, IT, EEE, ECE, MECHANICAL, ICE): ")
        while department.upper() not in ['CSE', 'IT', 'EEE', 'ECE', 'MECHANICAL', 'ICE']:
            print("Invalid department. Please enter a valid department.")
            department = input("Enter department again: ")

        return name, dob, email, phone_number, department, age

    @classmethod
    def validate_email(cls, email):
        students = StudentModel.read_students()
        if not re.match(r"[^@]+@gmail\.com", email):
            return False
        for student in students:
            if student.email == email:
                return False
        if email.lower() != email:
            return False
        return True

    @classmethod
    def display_students(cls, students, page_number=1):
        while True:
            if not students:
                print("No students found.")
                return

            page_size = 5
            start_index = (page_number - 1) * page_size
            end_index = min(start_index + page_size, len(students))

            headers = ["No.", "Name", "DOB", "Age", "Email", "Department"]
            data = []
            for i, student in enumerate(students[start_index:end_index], start=start_index + 1):
                data.append([i, student.name, student.dob, student.age, student.email, student.department])

            print(tabulate(data, headers=headers, tablefmt="grid"))

            print("\nOptions:")
            print("1. Next Page")
            print("2. Previous Page")
            print("3. Quit")

            choice = input("Enter your choice: ")
            if choice == "1":
                page_number += 1
            elif choice == "2":
                if page_number > 1:
                    page_number -= 1
                else:
                    print("You are already on the first page.")
            elif choice == "3":
                print("Quitting...")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    @classmethod
    def display_students_by_email(cls, email, students):
        found_students = [student for student in students if student.email == email]
        if not found_students:
            print("No student found with that email.")
            return

        headers = ["Name", "DOB", "Age", "Email", "Phone Number", "Department"]
        data = [[student.name, student.dob, student.age, student.email, student.phone_number, student.department] for student in found_students]
        
        print(tabulate(data, headers=headers, tablefmt="grid"))

    @classmethod
    def get_student_info_for_update(cls, email):
        students = StudentModel.read_students()
        found = False
        for student in students:
            if student.email == email:
                found = True
                break

        if not found:
            print("No student found with that email.")
            return

        name = input(f"Enter updated student name : ")
        while not re.match("^[A-Za-z ]{1,50}$", name):
            print("Invalid name format or length. Please enter a valid name (max 50 characters, format: Firstname Lastname).")
            name = input("Enter student name again: ")

        dob = input(f"Enter updated date of birth : ")
        while not cls.validate_dob(dob):
            print("Invalid date of birth. You must be older than 18 to register.")
            dob = input("Enter date of birth again (format: YYYY-MM-DD): ")

        phone_number = input(f"Enter updated phone number,(format: 10 digits): ")
        while not cls.validate_phone_number(phone_number):
            print("Invalid phone number. Please enter a 10-digit phone number.")
            phone_number = input("Enter phone number again: ")

        department = input(f"Enter updated department (CSE, IT, EEE, ECE, MECHANICAL, ICE): ")
        while department.upper() not in ['CSE', 'IT', 'EEE', 'ECE', 'MECHANICAL', 'ICE','cse','it','mechanical','eee','ece','ice','Mechanical']:
            print("Invalid department. Please enter a valid department.")
            department = input("Enter department again: ")

        age = cls.calculate_age(dob)

        new_student = {
            'name': name,
            'dob': dob,
            'phone_number': phone_number,
            'department': department,
            'age': age
        }

        StudentModel.update_student(email, new_student)
        print("Updated Successfully!")

    @classmethod
    def calculate_age(cls, dob):
        birth_date = datetime.strptime(dob, '%Y-%m-%d')
        age = (datetime.now() - birth_date).days // 365
        return age

    @classmethod
    def validate_dob(cls, dob):
        try:
            birth_date = datetime.strptime(dob, '%Y-%m-%d')
            age = (datetime.now() - birth_date).days // 365
            return age > 18
        except ValueError:
            return False

    @classmethod
    def validate_phone_number(cls, phone_number):
        return bool(re.match(r"^\d{10}$", phone_number))

    @classmethod
    def display_students_by_email(cls, email, students):
        found = False
        for student in students:
            if student.email == email:
                print(f"Name: {student.name}, DOB: {student.dob}, Age: {student.age}, Email: {student.email}, Phone Number: {student.phone_number}, Department: {student.department}")
                found = True
                break
        if not found:
            print("No student found with that email.")

# Example usage:
# students = StudentModel.read_students()
# StudentView.display_students(students, page_number=1)
