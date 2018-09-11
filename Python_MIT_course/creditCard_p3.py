# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 11:10:14 2017

@author: Mubeen
"""
balance = float(input("Balance: "))
annualInterestRate = float(input("Annual Interest Rate: "))
#monthlyPaymentRate = float(input("Monthly Payment Rate: "))
minMonPay = 0
mir = annualInterestRate/12.0
rem_balance = balance
upperBound = balance*((1+mir)**12)/12.0
lowerBound = balance/12.0
while (round(rem_balance,2) != 0.00):
    minMonPay = (upperBound + lowerBound)/2.0
    rem_balance = balance
    for i in range(12):
       # minMonPay = monthlyPaymentRate * balance
        monUnPayBal = rem_balance - minMonPay
        rem_balance = monUnPayBal + (monUnPayBal*mir)
    if round(rem_balance,2) > 0.00:
        lowerBound = minMonPay
    elif round(rem_balance,2) < 0.00:
        upperBound = minMonPay
#    print ("%.2f" % rem_balance)
#    print (minMonPay)


print ("Lowest Payment:" ,round(minMonPay,2))