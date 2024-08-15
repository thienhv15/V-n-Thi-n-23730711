# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:53:43 2024

@author: VanThien23730711
"""
print("Giải phương trình bậc nhất ax+b=0")
a = float(input("Nhap a:"))
b = float(input("Nhap b:"))
if a!= 0:
    print("Phương trình có nghiệm x=",-b/a)
else:
    if b!= 0:
     print("Phương trình vô nghiệm")
    else:
      print("Phương trình vô số nghiệm")
    