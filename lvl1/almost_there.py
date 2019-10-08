#LEVEL 1 PROBLEM 3 (ALMOST THERE)
# return true if a number is withing 10 digits + or - 100 and 200

def almost_there(num):
    if (num >= 90 and num <= 110) or (num >= 190 and num <= 210):
        return True
    else:
        return False

num = 201
print(almost_there(num))
