# Request the user to enter a sentence and save it under a variable called "str_ manip.

str_manip = input("Enter a sentence ;")

# Calculate and display the length of str_manip.

length_of_sentence = len(str_manip)
print(length_of_sentence)

# Find the last letter in str_manip

last_letter = str_manip[-1]

# Replace every occurrence of last_letter with "@"

str_manip_replaced_characters = str_manip.replace(last_letter, "@")

# print the sentence

print(str_manip_replaced_characters)

# print the last 3 characters in str_manip backwards 

last_three_characters_of_str_manip = str_manip[-1:-4:-1]
print(last_three_characters_of_str_manip)

# Create a five letter word that is made up of the first three characters and the last two characater 
# in str_manip.

first_three_characters_of_str_manip = str_manip[0:3:1]
last_two_characters_of_str_manip = str_manip[-1:-3:-1]
five_letter_word = first_three_characters_of_str_manip + last_two_characters_of_str_manip
print(five_letter_word)


