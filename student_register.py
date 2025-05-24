# Request the user to enter their student numbers
num_of_students_registering = int(input("How many students are registering: "))
# create a variable called student_numbers and make it a list
student_numbers = []

# Each time the loop runs the program Requests the user to enter the next student ID number.
for i in range(num_of_students_registering):
            student_number = input("Please enter your student number {}: ".format(i+1))
            student_numbers.append(student_number)

 # Write each of the ID numbers to a TextFile     
with open("reg_form.txt", "w") as file:
            for number in student_numbers:
                file.write(number + "\n")
# Include a dotted line after each student ID because 
# this document will be used as an attendance register, 
# which the students will sign when they arrive attheexamvenue.
                file.write("-------------------------------\n")  # Add a dotted line after each student number
        
print("The Student numbers have been written to reg_form.txt.")





