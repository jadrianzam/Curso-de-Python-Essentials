# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 20:50:23 2021

@author: Usuario
"""

"""
Escribir y probar una función que toma tres argumentos 
(un año, un mes y un día del mes) y devuelve el día correspondiente 
del año, o devuelve None si cualquiera de los argumentos no es válido.
"""

def isYearLeap(year):
    if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        return True
    else:
        return False


def daysInMonth(year, month):
    #print("Valor del mes en la función daysInMonth", month)
    dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year < 1582 or month < 1 or month > 12:
        return None
    if isYearLeap(year) and month == 2:
        return 29
    else:
        return dias[month - 1]


def dayOfYear(year, month, day):
    num_dias = 0
    for i in range(1, month):
        num_dias += daysInMonth(year, i)
    #print("Hasta el mes {} pasaron {} días".format(month - 1, num_dias))
    if day < 1 or day > daysInMonth(year, month):
        return None
    else:
        return num_dias + day
    
print(dayOfYear(1963, 4, 12))