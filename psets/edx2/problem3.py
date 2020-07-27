def retBalance(balance, aRate, payment):
    for i in range(12):
        balance = (1+aRate/12.0)*(balance-payment)
    return balance

def findMin(balance, aRate):
    low = balance/12
    high = (balance*(1+aRate/12.0)**12)/12.0
    epsilon = 0.01
    guess = (low+high)/2
    x = round(retBalance(balance, aRate, guess),2)
    while abs(x) >= epsilon:
        if x > 0:
            low = guess
        else:
            high = guess
        guess = (low+high)/2
        x = round(retBalance(balance, aRate, guess),2)

    return round(guess, 2)

print(findMin(393933333, 0.02))
