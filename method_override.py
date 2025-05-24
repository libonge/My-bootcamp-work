
# Define a class for representing adults with attributes like name, age, hair color, and eye color.
class Adult:
    def __init__(self, name, age, hair_color, eye_color):
        self.name = name
        self.age = age
        self.hair_color = hair_color
        self.eye_color = eye_color

    # Method to check if the adult can drive based on their age.
    def can_drive(self):
        print(f"{self.name} is old enough to drive.")

# Define a class for representing children, inheriting from the Adult class.
class Child(Adult):
    # Override the can_drive method for children, as they are too young to drive.
    def can_drive(self):
        print(f"{self.name} is too young to drive.")

# Function to check the driving ability of a person, considering their age and class.
def check_driving_ability(person):
    # Check if the person is an instance of Adult and is old enough to drive.
    if isinstance(person, Adult) and person.age >= 18:
        person.can_drive()
    else:
        # If not an adult or not old enough, call the can_drive method for children.
        person.can_drive()

# Collect user input to create a person object with relevant attributes.
name = input("Enter person's name: ")
age = int(input("Enter person's age: "))
hair_color = input("Enter person's hair color: ")
eye_color = input("Enter person's eye color: ")

# Check if the person is an adult or a child based on age.
if age >= 18:
    person = Adult(name, age, hair_color, eye_color)
else:
    person = Child(name, age, hair_color, eye_color)

# Call the function to check the driving ability of the person.
check_driving_ability(person)
