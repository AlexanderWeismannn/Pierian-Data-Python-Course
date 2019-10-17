#HOMEWORK QUESTION #5
#MULTIPLY A LIST BY EACH SUBSEQUENT NUMBER TO GET THE PRODUCT OF THE LIST
def multiply(numbers):
    total = 1 #so that the first number will multiply by 1 staying itself
    for i in range(len(numbers)):
        total = total*numbers[i]
    return total

num_list = [1,2,3,-4]
print(multiply(num_list))
