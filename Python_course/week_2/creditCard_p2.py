# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 11:10:14 2017

@author: Mubeen
"""
balance = float(input("Balance: "))
annualInterestRate = float(input("Annual Interest Rate: "))
#monthlyPaymentRate = float(input("Monthly Payment Rate: "))
minMonPay = 0
mir = annualInterestRate/12
rem_balance = balance
while (rem_balance > 0):
    minMonPay += 10
    rem_balance = balance
    for i in range(12):
       # minMonPay = monthlyPaymentRate * balance
        monUnPayBal = rem_balance - minMonPay
        rem_balance = monUnPayBal + (monUnPayBal*mir)
#    print ("%.2f" % rem_balance)
#    print (minMonPay)


print ("Lowest Payment:" ,minMonPay)
