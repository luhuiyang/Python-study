balance = 4213
annualInterstRate = 0.2
monthlyPaymentRate = 0.04

def getPrint(balance, annualInterstRate, monthlyPaymentRate):
    monthlyInterestRate = annualInterstRate / 12.0
    updatedbalanceeachmonth = balance
    
    for i in range (1, 13):
        minimummonthlypayment = monthlyPaymentRate * updatedbalanceeachmonth
        monthlyunpaidbalance = updatedbalanceeachmonth - minimummonthlypayment
        updatedbalanceeachmonth = monthlyunpaidbalance + (monthlyInterestRate * monthlyunpaidbalance)
        print 'Month: %d' % i
        print 'Minimum monthly payment: %.2f' % minimummonthlypayment
        print 'Remaining balance: %.2f' % updatedbalanceeachmonth
        
getPrint(balance, annualInterstRate, monthlyPaymentRate)