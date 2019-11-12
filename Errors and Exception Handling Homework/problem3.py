# PROBLEM #3
# USE THE TRY/EXCEPT/ELSE FUNCTIONALITY TO HANDLE AN ERROR
def ask(i):
    #square any integer entered
    return i**2
new_val = 0
while True:
    try:
        val = int(input("Input and Integer: "))
        new_val = ask(val)
    except:
        print("An error occured, please try again!")
        continue
    else:
        print("Thank you, you number squared is: {}".format(new_val))           
