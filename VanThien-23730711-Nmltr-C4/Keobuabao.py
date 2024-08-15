# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:24:42 2024

@author: VanThien23730711
"""

from random import randint

print("Nhap Bao, Búa, Kéo")

player = input()

computer = randint(0,2)


if computer == 0:

   computer = "Búa"

if computer == 1:

   computer = "Bao"

if computer == 2:

   computer = "Kéo"

print("-----")

print("Ban chon: " + player)

print("May chon: " + computer)

print("-----")


if computer == player: 

 print("Hòa")

else:
   if player == "Bao":

      if computer == "Búa":

         print("Thắng")

      else:

         print("Thua")


   elif player == "Búa":

      if computer == "Kéo":

         print("Thắng")

      else:

         print("Thua")


   elif player == "Kéo":

      if computer == "Bao":

         print("Thắng")

      else:

         print("Thua")
   
   else:

     print("Nhap sai!")