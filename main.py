# from student_controller import StudentController

# class StudentManagementSystem:
#     def __init__(self):
#         self.student_controller = StudentController()

#     def start(self):
#         while True:
#             print("""
#             ------------------------------------------------------------
#             Student Management System
#             ------------------------------------------------------------
#             1. Create Student
#             2. Read Students
#             3. View Student by Email
#             4. Update Student
#             5. Delete Student
#             6. Exit
#             """)

#             choice = input("Enter your choice: ")

#             if choice == '1':
#                 self.student_controller.create_student()
#             elif choice == '2':
#                 self.student_controller.read_students()
#             elif choice == '3':
#                 self.student_controller.view_student_by_email()
#             elif choice == '4':
#                 self.student_controller.update_student()
#             elif choice == '5':
#                 self.student_controller.delete_student()
#             elif choice == '6':
#                 print("Thanks! Bye.")
#                 break
#             else:
#                 print("Invalid choice. Please enter a valid option.")

# if __name__ == "__main__":
#     sms = StudentManagementSystem()
#     sms.start()



from student_controller import StudentController

class StudentManagementSystem:
    def __init__(self):
        self.student_controller = StudentController()

    def start(self):
        while True:
            print("""
            ------------------------------------------------------------
            Student Management System
            ------------------------------------------------------------
            1. Create Student
            2. Read Students
            3. View Student by Email
            4. Update Student
            5. Delete Student
            6. Exit
            """)

            choice = input("Enter your choice: ")

            if choice == '1':
                self.student_controller.create_student()
            elif choice == '2':
                self.student_controller.read_students()
            elif choice == '3':
                self.student_controller.view_student_by_email()
            elif choice == '4':
                self.student_controller.update_student()
            elif choice == '5':
                self.student_controller.delete_student()
            elif choice == '6':
                print("Thanks! Bye.")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.start()
