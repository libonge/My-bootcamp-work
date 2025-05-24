
class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    def head_office_location(self):
        print("Head office location: Cape Town")

class OOPCourse(Course):
    def __init__(self):
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"

    def trainer_details(self):
        print("Course:", self.description)
        print("Trainer:", self.trainer)

    def show_course_id(self):
        print("Course ID: #12345")

class Adult:
    def can_drive(self):
        print("You are old enough to drive.")

class Child:
    def can_drive(self):
        print("You are not old enough to drive.")

# Create an instance of OOPCourse
course_1 = OOPCourse()

# Call the methods and display the results
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()

# Determine user's age
user_age = int(input("How old is the person ? ")) # Replace with actual user age

# Create an instance of Adult or Child class based on user's age
if user_age >= 18:
    person = Adult()
else:
    person = Child()

# Call the can_drive() method based on the user's age
person.can_drive()

