 # Request user to enter their full_name 

full_name = input("Please enter your full_name : \n")

# Validate the full_name entered by the user and if they haven't
# print error message
if len (full_name) == 0:
        print ("You have entered anything. Please enter your full_name")

# Validate the full_name entered by  the user and if they haven't 
#  print error message 
elif len (full_name) < 4:
     print("You have entered less than 4 chars please make sure you entered your name and surname")
     #chars stands for characters

# Validate the full_name entered by the user and if they haven't 
# print error message

elif len (full_name) > 25: 
       print("You have entered more than 25 chars please make sure that you entered only your full_name")
       
# Validate the full_name entered by the user and if they have 
# print message of apprecaiton for their cooperation

else: 
      len (full_name) > 4 
      print("Thank you for entering your name ")


            





