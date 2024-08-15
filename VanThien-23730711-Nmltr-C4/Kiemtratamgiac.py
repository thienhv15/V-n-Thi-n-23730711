# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:13:22 2024

@author: VanThien 23730711
"""
print("Kiểm tra tam giác")
a = float(input("Nhap a:"))
b = float(input("Nhap b:"))
c = float(input("Nhap c:"))
if a+b>c and a+c>b and b+c>a:
   if a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
       print("loaiTamGiac = 'vuông'")
   elif a==b and b==c:
       print("loaiTamGiac = 'đều'")
   elif a==b or a==c or b==c:
       print("loaiTamGiac = 'cân'")
   elif a*a > b*b+c*c or b*b > a*a+c*c or c*c > a*a+b*b:   
       print("loaiTamGiac = 'tù'")
   else:
       print("loaiTamGiac = 'nhọn'")
