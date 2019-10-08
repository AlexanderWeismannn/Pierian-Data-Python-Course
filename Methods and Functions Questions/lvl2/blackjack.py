#LEVEL 2 PROBLEM 3 (BLACKJACK)
# GIVEN 3 INT'S BETWEEN 1 AND 11, SEE IF THE SUM IS <= TO 21

def blackjack(num1,num2,num3):
    numSum = num1 + num2 + num3
    if (numSum > 21):
        if(num1 == 11 or num2 == 11 or num3 == 11):
            numSum = numSum - 10;
            if(numSum <= 21):
                    return numSum
        else:
            return "BUST"

        return "BUST"

    else:
        return numSum

a = 5
b = 6
c = 7

print(blackjack(a,b,c))
