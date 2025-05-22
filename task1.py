#Create a variable called num and set it to 5
num = 5 
 
# increasing star pattern
for i in range(1, num*(4-2)):
  if i <= num:
     print('*' * i )
     
# Decreasing stars pattern
  else:
    print('*' * (num*(4-2) -i ))
