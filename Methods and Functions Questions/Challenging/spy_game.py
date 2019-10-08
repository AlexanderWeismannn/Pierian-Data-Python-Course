#CHALLENGING PROBLEMS #1 (SPY GAME)
#TAKES IN A LIST OF NUMS AN RETURNS TRUE if there exists a [0, 0, 7] in order

def spy_game(nums):
    exists = 0# if the number reaches 3 then the 007 string exists in order
    for i in range(len(nums)):
        if(nums[i] == 0 and exists == 0):
            exists = exists + 1
            continue
        if(nums[i] == 0 and exists == 1):
            exists = exists + 1
            continue
        if(nums[i] == 7 and exists == 2):
            exists = exists + 1


    if(exists == 3):
        return True
    else:
        return False

print(spy_game([1,7,2,0,4,5,0]))
