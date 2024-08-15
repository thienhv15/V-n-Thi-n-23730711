# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:23:48 2024

@author: VanThien23730711
"""

s = input("Nhập ngày, tháng, năm (dd/mm/yyyy): ")

try:
    ngay, thang, nam = map(int, s.split('/'))
except ValueError:
    print("Định dạng ngày không hợp lệ.")
else:
    if nam % 400 == 0 or (nam % 4 == 0 and nam % 100 != 0):
        Check = True
    else:
        Check = False

    x = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if Check:
        x[1] = 29

    if nam < 1:
        print("Năm không hợp lệ.")
    elif thang < 1 or thang > 12:
        print("Tháng không hợp lệ.")
    elif ngay < 1 or ngay > x[thang - 1]:
        print("Ngày không hợp lệ.")
    else:
        print("Ngày, tháng, năm hợp lệ.")