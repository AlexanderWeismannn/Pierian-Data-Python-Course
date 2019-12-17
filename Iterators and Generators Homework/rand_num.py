#GENERATOR THAT YIELDS (N) RANDOM NUMBERS BETWEEN (LOW/HIGH)
import random

def rand_num(low, high, n):
    for i in range(n):
        yield(random.randint(low,high))

for num in rand_num(1,10,2):
    print(num)
