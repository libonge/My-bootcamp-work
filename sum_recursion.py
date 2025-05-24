# Function that takes a list of numbers and an index as arguments
def sum_recursion(numbers, index):

   # If the index is 0, return the value at that index
    if index == 0 :
        return numbers[0]
    
    # If the index is not 0
        # Return the value at the current index plus the result of repeatedly calling the function with the index declined by 1
    else:
        return numbers[index] + sum_recursion(numbers, index - 1)

# List of numbers
my_list_of_numbers= [30, 20, 40, 50, 60, 70, 80]

# Index point
my_index = 4

# Call the sum_recursion function with the list and index as arguments and store the result
result = sum_recursion(my_list_of_numbers, my_index)

# print the result, which should be 200 if index point is 4
print(result)



