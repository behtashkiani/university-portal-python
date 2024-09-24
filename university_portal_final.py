# List of professors with their lecture's codes
professors = [
    {'name': 'Prof Maturo', 'username': 'PR01'},
    {'name': 'Prof Romano', 'username': 'IS02'},
    {'name': 'Prof Maturo', 'username': 'SL03'},
    {'name': 'Prof Marulli', 'username': 'OP04'},
    {'name': 'Prof Iacono', 'username': 'CS05'},
    {'name': 'Prof Marulli', 'username': 'AN06'},
    {'name': 'Prof Irpino', 'username': 'DV07'},
    {'name': 'Prof Maturo', 'username': 'ER08'},
    {'name': 'Prof Irpino', 'username': 'FR09'},
    {'name': 'Prof Verde', 'username': 'FM09'},
    {'name': 'Prof De Lucia', 'username': 'EC10'},
    {'name': 'Prof Iacono', 'username': 'NM11'},
    {'name': 'Prof De Lucia', 'username': 'EN12'},
]

# List of 5 students as default with their additional information
students = [
    {'name': 'BEHTASH KIANI', 'username': 'S0034118', 'password': '12318', 'date_of_birth': '22/02/1998'},
    {'name': 'KAMAND ZARGAR', 'username': 'S0034119', 'password': '12319', 'date_of_birth': '28/07/2001'},
    {'name': 'RAMTIN RAFIEE', 'username': 'S0034120', 'password': '12320', 'date_of_birth': '05/02/1997'},
    {'name': 'KEYWAN KIANUSCH', 'username': 'S0034121', 'password': '12321', 'date_of_birth': '19/08/1997'},
    {'name': 'AMIR MIRZAEIAN', 'username': 'S0034122', 'password': '12322', 'date_of_birth': '19/09/1998'},
]
# List of availabe courses with their code
available_courses = [
    {'name': 'Probability', 'code': 'PR01'},
    {'name': 'Inferential Statistics', 'code': 'IS02'},
    {'name': 'Statistical Learning', 'code': 'SL03'},
    {'name': 'Object-oriented Programming', 'code': 'OP04'},
    {'name': 'Computer Science', 'code': 'CS05'},
    {'name': 'Analysis', 'code': 'AN06'},
    {'name': 'Data Visualization', 'code': 'DV07'},
    {'name': 'Experimental Research Design', 'code': 'ER08'},
    {'name': 'French', 'code': 'FR09'},
    {'name': 'Financial Mathematics', 'code': 'FM09'},
    {'name': 'Economics', 'code': 'EC10'},
    {'name': 'Numerical Methods', 'code': 'NM11'},
    {'name': 'English', 'code': 'EN12'},
]

# Security question with it's answer. 
security_questions_and_answers = [
    {'question': 'What is the name of your Pet?', 'answer': 'LOCA'},
]

# Student Class where each student has a unique name, unique username, password and date of birth
class Student:
    def __init__(self, name, username, password, date_of_birth):
        self.name = name
        self.username = username
        self.password = password
        self.date_of_birth = date_of_birth
        # As default every student has these 5 courses in their study plan (like our's in first semester)
        self.study_plan = ["Analysis", "Computer Science", "Probability", "Economics"]
    
    # Fucntion to add a course to the study plan. Cannot exceed more than 6 in a semester
    def add_course(self, course):
        if len(self.study_plan) >= 6:
            print("Error: You've reached your maximum amount of courses for this semester.")
        else:
            self.study_plan.append(course)

    # Fucntion to remove the course. Students cannot have less than 2 courses. 
    def remove_course(self):
        if len(self.study_plan) <= 2:
            print("Error: You cannot have less than 2 courses in a semester.")
        else:
            course_to_remove = input("Enter the course you want to remove: ")
            if course_to_remove in self.study_plan:
                self.study_plan.remove(course_to_remove)
                print(f"{course_to_remove} removed from your study plan.")
            else:
                print(f"Error: {course_to_remove} is not in your study plan. Please try again.")


    # This function lets the user to see its courses in their study plan. 
    def view_courses(self):
        print("\nYour Study Plan:")
        for course in self.study_plan:
            print(course)


# Lecturer class where each lecturer has a name, a corrisponding code, and a list of courses taught
class Lecturer:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.courses_taught = []

    def add_course_taught(self, course_code):
        self.courses_taught.append(course_code)

    #def add_course_taught(self, course):
     #   self.courses_taught.append(course)

    def view_courses_taught(self):
        print("Courses Taught by the Lecturer:")
        for course in self.courses_taught:
            print(course)

class UniversityPortal:
    professors = professors
    students = students
    available_courses = available_courses
    #security_questions_and_answers = security_questions_and_answers

    def __init__(self):
        self.registered_students = []
        self.registered_lecturers = []

    def register_student(self, student):
        self.registered_students.append(student)


# we are not using it anymore...
    def register_lecturer(self, lecturer):
        self.registered_lecturers.append(lecturer)

    def check_who_is_teaching(self, student):
        course_name = input("Enter the course code:\n")
        # Placeholder: Implementation for checking who is teaching a course
        for lecturer in self.registered_lecturers:
            if course_name in lecturer.courses_taught:
                print(f"Professor {lecturer.name} is teaching {course_name} for this semester.")
                return
        print(f"No information found for {course_name}.")

    def forget_password(self, username, answer):
        # Placeholder: Implementation for forget password
        security_answer = input("Answer the security question: ")
        birthdate = input("Enter your birthdate (DD/MM/YYYY): ")

        if (
            security_answer.lower() == security_questions_and_answers[0]['answer'].lower()
            and birthdate == students[0]['date_of_birth']
        ):
            print(f"Very good {username}! Your password is {students[0]['password']}.")
        else:
            print("Wrong information. Please try again.")

    def display_student_menu(self, student):
        print(f"\nWelcome to the university portal {student.name}.")
        print("1. View My Courses")
        print("2. Add Course to Study Plan")
        print("3. Remove Course from Study Plan")
        print("4. Who is Teaching?")
        print("5. Logout")

    def display_available_courses(self, student):
        print("\nAvailable Courses:")
        for index, course in enumerate(self.available_courses, start=1):
            if course['name'] not in student.study_plan:
                print(f"{index}. {course['name']} ({course['code']})")

    def student_menu(self, student):
        while True:
            self.display_student_menu(student)
            choice = input("Enter your choice: ")

            if choice == '1':
                student.view_courses()
            elif choice == '2':
                self.display_available_courses(student)
                course_index = input("Enter the number of the course you want to add: ")
                try:
                    course_index = int(course_index)
                    selected_course = self.available_courses[course_index - 1]['name']
                    student.add_course(selected_course)
                    print(f"\n{selected_course} added to your study plan.")
                except (ValueError, IndexError):
                    print("Invalid input. Please try again.")
            elif choice == '3':
                student.remove_course()
            elif choice == '4':
                self.check_who_is_teaching(student)
            elif choice == '5':
                print(f"Goodbye {student.name}! Have a great day.")
                break
            else:
                print("Invalid choice. Please try again.")

    def run_portal(self):
        while True:
            #print("\nWelcome to the University Portal!")
            print("1. Log In")
            print("2. Register")
            print("3. More Info about Us")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                username = input("Enter your username: ")
                password = input("Enter your password: ")

# The python next function is used to return the next item from the iterator 
# If there are no items present, the iterator gets exhausted
                student = next((s for s in self.registered_students if s.username == username), None)
                if student and student.password == password:
                    print("Logged in successfully.")
                    self.student_menu(student)
                else:
                    print("Invalid credentials. Please try again.")
            elif choice == '2':
                print("\nSend your documents to this email address to register. It might take up to 4 working days.")
                print("Email: register.here@uniimaginary.it")
            elif choice == '3':
                print("\nNaples, Via Benedetto Brin 67 80142")
                print("Tel: 3558999900")
            elif choice == '4':
                print("\nGoodbye! Have a great day.")
                break
            else:
                print("\nInvalid choice. Please try again.")

# Main program
if __name__ == "__main__":
    # This line of code starts the university portal.
    university_portal = UniversityPortal()

    # Create student instances
    for student_info in students:
        #To unpack the values from the tuples and dictionary,
        #we use the * operator for the tuples and the ** operator for the dictionary in the function call
        student = Student(**student_info)
        university_portal.register_student(student)

    # Create lecturer instances
    for lecturer_info in professors:
        lecturer = Lecturer(name=lecturer_info['name'], code=lecturer_info['username'])
        lecturer.add_course_taught(lecturer_info['username']) 
        university_portal.register_lecturer(lecturer)

    # Run the portal
    university_portal.run_portal()
