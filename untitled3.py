# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 03:39:44 2023

@author: Hp
"""

import math
a=int(input("Enter First Side:"))
b=int(input("Enter Second Side:"))
c=int(input("Enter Third Side:"))

s=(a+b+c)/2

area=math.sqrt(s*(s-a)*(s-b)*(s-c))