#LEVEL 1 PROBLEM 1 (OLD MACDONALD)
#capitalize the 1st and 4th letter of any word
def old_macdonald(name):
    newName = name[:0] + name[0].upper() + name[1:3] + name[3].upper() + name[4:]
    return(newName)

name = "macdonald"
print(old_macdonald(name))
