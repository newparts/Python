# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 13:11:06 2019

@author: iuliu
"""

import csv

x = []
y = []

with open('CSV3.csv') as f:
    reader = csv.reader(f, delimiter=',')
    line_count = 0
    for row in reader:
        x.append(float(row[0]))
        y.append(float(row[1]))

print(x)
print(y)

mx = 0
my = 0

for i in range(0, len(x)):
    mx += x[i]
    my += y[i]

mx /= len(x)
my /= len(y)

print(mx)
print(my)

beta_top = .0
beta_bot = .0

for i in range(len(x)):
    beta_top += (x[i] - mx)*(y[i] - my)
    beta_bot += (x[i] - mx)**2

beta = beta_top/beta_bot
print(beta)

alpha = my - beta*mx

rez = alpha+beta*100
print(alpha)
print(rez)