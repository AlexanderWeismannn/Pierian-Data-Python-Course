#HOMEWORK QUESTION #2
#CHECKS IF A NUMBET IS BETWEEN A CERTAIN RANGE

def ran_check(num,low,high):
    if (num >= low) and (num <= high):
        return print("{} is in the range between {} and {}".format(num,low,high))
    else:
        return print("Not in range")

ran_check(5,2,7)
