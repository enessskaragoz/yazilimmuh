# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 21:15:32 2022

@author: Enes
"""

# HESAP MAKİNESİ

print(""" ***********************************************************
    Transactions : 
    1. Addition
    2. Division
***********************************************************
 """)

a = int(input("First number : "))
b = int(input("Second number : "))

Transaction = input("Select Transaction: ")

if Transaction == "1":
   print("{} + {} = {}".format(a,b,a+b)) 
   