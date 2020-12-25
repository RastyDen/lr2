#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
X1 = float(input("Введите координату x1: "))
Y1 = float(input("Введите координату y1: "))
X2 = float(input("Введите координату x2: "))
Y2 = float(input("Введите координату y2: "))
X3 = float(input("Введите координату x3: "))
Y3 = float(input("Введите координату y3: "))
X4 = float(input("Введите координату x4: "))
Y4 = float(input("Введите координату y4: "))
A = math.sqrt((X1-X2)**2+(Y1-Y2)**2)
B = math.sqrt((X2-X3)**2+(Y2-Y3)**2)
C = math.sqrt((X3-X4)**2+(Y3-Y4)**2)
D = math.sqrt((X4-X1)**2+(Y4-Y1)**2)
dia = math.sqrt((X1-X3)**2+(Y1-Y3)**2)
p1 = (A+B+dia)/2
p2 = (C+D+dia)/2
S1 = math.sqrt(p1*(p1-A)*(p1-B)*(p1-dia))
S2 = math.sqrt(p2*(p2-C)*(p2-D)*(p2-dia))
S = S1+S2
print("Площадь четырехугольника равна  %.2f" % S)