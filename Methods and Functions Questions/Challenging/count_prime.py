#CHALLENGING PROBLEMS #2 (COUNT PRIMES)
# DISPLAYS ALL PRIME NUMBERS UP TO THE VALUE POSTED

def count_primes(num):
    new_list = []
    for x in range(2,num+1):# range is exclusive
        prime = True
        for i in range(2,x):
            if(x%i == 0):
                prime = False
        if prime:
            new_list.append(x)

    return new_list

num = 97
print(count_primes(num))
