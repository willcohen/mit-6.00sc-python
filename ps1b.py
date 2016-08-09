# Problem Set 1

outstanding = float(raw_input('Enter the outstanding balance on your'
                              + ' credit card: '))
interestrate = float(raw_input('Enter the annual credit card interest'
                               + ' rate as a decimal: '))
minpay = 0
balance = outstanding

while balance > 0:
    minpay += 10
    updatedbalance = outstanding
    for x in range(0, 12):
        x += 1
        monthlyinterest = interestrate/12.0
        updatedbalance = updatedbalance * (1 + monthlyinterest) - minpay
        if updatedbalance < 0:
            break
    balance = updatedbalance

print 'RESULT'
print 'Monthly payment to pay off debt in 1 year: ' + str(int(minpay))
print 'Number of months needed: ' + str(x)
print 'Balance: ' + str(round(balance, 2))
