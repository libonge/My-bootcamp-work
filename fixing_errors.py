
# Syntax error
# The welcome message was not assigned to a variable
welcome_message = "Welcome to the error program"
print(welcome_message )

#no paranthesis and incorrect Indentation
print("\n")

#Syntax error
#The "==" are used for comparison not for assigning values
age_Str = "24 years old"

# Indentation error and Runtime error
#age variable was not correctly cast to an integer
age = int(24)

#Runtime error 
# no paranthesis and no curly braces for age variable for f-string format
print(f"I'm {age} years old.")

# Runtime error
# years from now value was not cast to an integer
# which is the integer 3 
years_from_now = int(3)

#Syntax error
#variable age was not defined
#for calculatiions
total_years =(age) + years_from_now

#runtime errror and indentation error
# no paranthesis and curly braces for f-string
print (f"The total number of years : {total_years}")

#Syntax error
#variable value (total) was not complete, years was missing
total_months = total_years * 12


#Syntax error
# value of the variable was not defined
animal = "Lion"

animal_type = "cub"
number_of_teeth = 16


# Logical error
# Varables incorrectly positioned.
# missing f-string format

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"

# Runtime error
# missing paranthesis
print (full_spec)


#Logical error
#Total months were short by 6 months to produce a total of 330 months
total_months = total_months + int(6)
print(total_months)

#Runtime error and syntax error
#missing paranthesis and no curly braces for the correctm vaiable for f-string
#incorrect variable was used total months is the correct one
print(f"In 3 years and 6 months, I'll be {total_months} months old")



