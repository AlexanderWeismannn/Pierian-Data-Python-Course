#HOMEWORK QUESTION #3
#COUNTS THE NUMBERS OF LOWERCASE AND UPPERCASE OCCURENCES IN A STRING

def up_low(s):
    uppers = 0
    lowers = 0
    for x in s:
        if(x.isupper()):
            uppers = uppers + 1
        elif(x.islower()):
            lowers = lowers + 1

    return print("No. of Upper case characters: {} \nNo. of Lower case characters: {}".format(uppers,lowers))

s = "Hello Mr. Rogers, how are you this fine Tuesday?"
up_low(s)
