#LEVEL 2 PROBLEM 2 ( PAPER DOLL)
#RETURN A STIRING WHERE EVERY CHAR IS DUPLICATED 3 TIMES

def paper_doll(text):
    stretched_word = ""
    for i in range(len(text)):
        stretched_word = stretched_word + text[i] + text[i] + text[i]
    return stretched_word

text = "Hello"
print(paper_doll(text))
