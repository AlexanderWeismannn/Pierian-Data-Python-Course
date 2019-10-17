#HOMEWORK CHALLENGE PROBLEM
#CHECKS IF A STRING IS A PANGRAM(CONTAINS EVERY LETTER IN THE ALPHABET)

import string
def ispangram(str1, alphabet = string.ascii_lowercase):
    counter = 0#checks all letters exist(i.e 26)
    ispan = False
    str1.lower()#set the string to lower so as to compare it to the lowercase alphabet

    for i in range(len(alphabet)):
        if alphabet[i] in str1:
            counter = counter + 1
    if counter == 26:
        ispan = True

    return ispan

str = "The quick brown fox jumps over the lazy dog"
print(ispangram(str))
