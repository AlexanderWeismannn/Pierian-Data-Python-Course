#HOMEWORK QUESTION #4
#CREATE A NEW LIST OF UNIQUE VALUES FROM A LIST THAT CONTAINS DUPLICATES
def unique_list(lst):
    exists = False#switcher to see if a value exits in a list
    new_list = []#the new list that will consist of only unique values
    new_list.append(lst[0])
    for i in range(0,len(lst)):
        for x in range(len(new_list)):
            if lst[i] == new_list[x]:
                exists = True

        if exists == False:
            new_list.append(lst[i])

        exists = False
    return new_list

vals = [2,3,3,3,4,5,5]
print(unique_list(vals))
