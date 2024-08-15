# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:07:03 2024

@author: VanThien 23730711
"""
print("Kiểm tra ba cạnh của tam giác")
a = float(input("Nhap a:"))
b = float(input("Nhap b:"))
c = float(input("Nhap c:"))
if a+b>c and a+c>b and b+c>a:
   print("{}, {}, {} la ba canh cua mot tam giac".format(a, b, c))
else:
   print("{}, {}, {} khong la ba canh cua mot tam giac".format(a, b, c))
