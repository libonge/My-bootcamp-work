# Request the user to input their time of completion
# For each activity.

# Request user for swimming Time :
swimming_time = int(input("How many minutes did you take to swim ? "))

# Request user for cycling time :
cycling_time =  int(input("How many minutes did you take to cycle  ? " ))

# Request user for running time :
running_time = int(input("How many minutes did you take to run ? "))

# Add up all the time for each activtiy and print it as one :
completion_time =  swimming_time + running_time + cycling_time

print ( f" Time taken to complete triathlon :   {completion_time} ")

# If completion_time is less than or equal to 100
#  Award Provincial colours :
if completion_time <= 100:
    print ("Congratulations you have been awarded a Provincial colours !")

# If completion_time is less than or equal to 105
# Award Provincial half colours :
elif completion_time <= 105:
    print("Congratulations you have been awarded Provincial half colours !")

# If completion_time is less than or equal to 110
# Award Provincial half colours :
elif completion_time <= 110:
   print("Congratulations you have been awarded a Provincial scroll")

# If completion_time is greater than 110
# Do not give award
else:
  print("Unfortunately your time of completion is not awarded anything.")
      
