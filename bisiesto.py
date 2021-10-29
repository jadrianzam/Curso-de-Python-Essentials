# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 10:54:14 2021

@author: JAZM
"""

anio = int(input("Escriba un año: "))

if (anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)):
    print("Es bisiesto")
else:
    print("No es bisiesto")
        
    