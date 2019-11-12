#PROBLEM #2
# USING THE TRY/EXCEPT FUNCTIONALITY TO CATCH THE ANOTHER ERROR

x = 5
y = 0
try:
    z = x/y
except:
    print("You can't divide by 0!")
finally:
    print("All Done")
