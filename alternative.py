#Request the user to enter their name
sentence = input(" Enter a sentence : ")
string = ""

#Programme that will make each alternate character case uppercase
#or each character lowercase
for i in range (len(sentence)):

    if i % 2 == 1:
         
      string += sentence[i].lower()
    else: 
         
       string += sentence[i].upper()
 
print(string)

#Request the user to enter their name

sentence = input(" Enter a sentence : ")
words = sentence.split()

# Programme that will make each alternate word case uppercae
# or each word lowercase
for i in range(len(words)):

    if i % 2 == 0:
    
       words[i] = words[i].upper()
    else :
       words[i] = words[i].lower()
    
    sentence = ' '.join(words)

final_sentence = (words)
    
print(final_sentence)


