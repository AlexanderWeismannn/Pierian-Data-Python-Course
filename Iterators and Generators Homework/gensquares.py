#USES A GENERATOR TO YIELD A "list" FROM 0 - X
#SAVING ON MEMORY
def gensquares(N):
    for x in range(N):
        yield(x**2)

for x in gensquares(10):
    print(x)
