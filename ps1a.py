# Problem Set 1

outstanding = float(raw_input('Enter the outstanding balance on your'
                              + ' credit card: '))
interestrate = float(raw_input('Enter the annual credit card interest'
                               + ' rate as a decimal: '))
minimumrate = float(raw_input('Enter the minimum monthly payment rate'
                              + ' as a decimal: '))
total = 0

for x in range(0, 12):
    x += 1
    print 'Month:', x
    minpay = minimumrate * outstanding
    print 'Minimum monthly payment: $' + str(round(minpay, 2))
    interestpaid = interestrate/12.0 * outstanding
    principalpaid = minpay - interestpaid
    print 'Principal paid: $' + str(round(principalpaid, 2))
    outstanding = outstanding - principalpaid
    print 'Remaining balance: $' + str(round(outstanding, 2))
    total = total + interestpaid + principalpaid

print 'RESULT'
print 'Total amount paid: $' + str(round(total, 2))
print 'Remaining balance: $' + str(round(outstanding, 2))
