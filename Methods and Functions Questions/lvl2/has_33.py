#LEVEL 2 PROBLEM 1 (HAS 33)
#SEE IF AN ARRAY CONTAINS A 3 NEXT TO ANOTHER 3

def has_33(nums):
    for i in range(len(nums)):
        if (nums[i] == 3):
            if nums[i+1] == 3:
                return True
    else:
        return False



nums = [1,3,3,1]
wrong_nums = [3,1,3,1]
print(has_33(nums))
