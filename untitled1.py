# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 03:11:20 2023

@author: Hp
"""

p=int(input("Enter the principle amount"))
r=int(input("Enter the rate"))
n=int(input("Enter the time"))
emi=p*r*(1+r)^n/(1+r)^n-1
print(emi)