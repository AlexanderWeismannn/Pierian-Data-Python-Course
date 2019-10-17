#HOMEWORK QUESTION #6
# Determines if a word is palindrome by flipping the word and comparing it
def palindrome(s):
    new_s = s[::-1]#reverses the original string
    return s == new_s


word = "helleh"
print(palindrome(word))
