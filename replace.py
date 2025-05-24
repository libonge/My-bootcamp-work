#Create a variable called sentence and store the string "The!quick!brown!fox!jump!over!the!lazy!dog"

sentence = "The!quick!brown!fox!jump!over!the!lazy!dog" # This is a single string, due to qoutation marks.

# Use the replace() function to replace every "!" with a blank space and print.
sentence = sentence.replace("!" , " ")
print(sentence)

#  Use the upper function to Capitalize the whole sentence and print 
sentence = sentence.upper()
print(sentence)

# Reprint the sentence in reverse using slicing.

sentence = sentence  [ ::-1 ]
print(sentence)



