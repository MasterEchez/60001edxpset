def retBalance(balance, aRate, payment):
    for i in range(12):
        balance = (1+aRate/12.0)*(balance-payment)
    return balance

def findMin(balance, aRate):
    result = 0

    while round(retBalance(balance, aRate, result),2) >= 0:
        result += 10
    return result

print(findMin(3926, 0.2))
