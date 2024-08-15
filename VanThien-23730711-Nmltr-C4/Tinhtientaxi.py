# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:45:47 2024

@author: VanThien23730711
"""

km = float(input("Nhập số km quãng đường đi được: "))
tong_tien = 0
if km <= 0:
    print('Số km không hợp lệ')
if km <= 1:
    tong_tien0 = km * 20000
    tong_tien += tong_tien0
if  1 < km <= 3:
    tong_tien1 = km * 13000
    tong_tien += tong_tien1
if 4 <= km <= 8:
    tong_tien2 =  39000 + (km - 3) * 12000
    tong_tien += tong_tien2

if km > 8:
    tong_tien3 = 99000 + (km-8) * 10000
    tong_tien += tong_tien3
if tong_tien > 100000:
        tong_tien *= 0.92 
print('Tổng tiền taxi',tong_tien,'VND')