#LEVEL 2 PROBLEM 4 (SUMMER OF 69 )
#GET THE SUM OF THE ARRAY, IGNORING ALL THE NUMBERS BETWEEN 6 AND 9

def summer_69(arr):
    total = 0
    addNum = True #a swapper val that decides when a num should be added
    for i in range(len(arr)):
        if(arr[i] == 6):
            addNum = False
        if(arr[i] == 9 and addNum == False):
            addNum = True
            continue
        if(addNum == True):
            total = total + arr[i]

    return total

arr = [1,3,5]
arr2 = [4,5,6,7,8,9]
arr3 = [2,1,6,9,11]
print(summer_69(arr3))
