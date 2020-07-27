def retBalance(balance, aRate, mRate):
    for i in range(12):
        balance = (1+aRate/12.0)*(balance)*(1-mRate)
    return round(balance, 2)

print(retBalance(42, 0.2, 0.04))