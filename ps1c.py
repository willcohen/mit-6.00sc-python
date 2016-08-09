# Problem Set 1

outstanding = float(raw_input('Enter the outstanding balance on your'
                              + ' credit card: '))
interestrate = float(raw_input('Enter the annual credit card interest'
                               + ' rate as a decimal: '))
minpay = 0
balance = outstanding

lowerbound = balance / 12.0
upperbound = (balance * (1 + (interestrate / 12.0)) ** 12.0) / 12.0
midpoint = (upperbound + lowerbound) / 2.0

while abs(upperbound - lowerbound) > 0.0001:
    midpoint = (upperbound + lowerbound) / 2.0
    minpay = midpoint
    updatedbalance = outstanding
    for x in range(0, 12):
        x += 1
        monthlyinterest = interestrate/12.0
        updatedbalance = updatedbalance * (1 + monthlyinterest) - minpay
        # if updatedbalance < 0:
        # break
    balance = updatedbalance
    if balance > 0:
        lowerbound = midpoint
    if balance < 0:
        upperbound = midpoint

print 'RESULT'
print 'Monthly payment to pay off debt in 1 year: ' + str(round(minpay, 2))
print 'Number of months needed: ' + str(x)
print 'Balance: ' + str(round(balance, 2))
