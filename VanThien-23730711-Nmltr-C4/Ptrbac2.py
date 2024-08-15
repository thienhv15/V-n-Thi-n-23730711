# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:57:53 2024

@author: VanThien23730711
"""

import math
print("Giải phương trình bậc 2: ax2 + bx + c = 0 (a khác 0)")
a = float(input("Nhập hệ số a: "))
if a == 0:
    print("Số a phải khác 0")       
b = float(input("Nhập hệ số b: "))        
c = float(input("Nhập hệ số c: "))
delta = b**2 - 4 * a * c
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print("Phương trình có nghiệm kép x1 = x2 = ", -(b / (2 * a)) )
else:
    print("Phương trình có hai nghiệm phân biệt:")
    print("x1= ", (-b+math.sqrt(delta))/(2*a)) 
    print("x2= ", (-b-math.sqrt(delta))/(2*a))
  
          
          