#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 11:10:14 2017

@author: Mubeen
"""
balance = float(input("Balance: "))
annualInterestRate = float(input("Annual Interest Rate: "))
monthlyPaymentRate = float(input("Monthly Payment Rate: "))
mir = annualInterestRate/12
for i in range(12):
    minMonPay = monthlyPaymentRate * balance
    monUnPayBal = balance - minMonPay
    balance = monUnPayBal + (monUnPayBal*mir)
    #print ("%.2f" % balance)
print ("Remaining balance: %.2f" % balance)
