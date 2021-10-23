# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 07:30:38 2021

@author: Adrián Zambrano
"""

print("Empezando a trabajar con Python")
print("Realizado por: Adrián Zambrano\n")

print("Consultando los tipos de valores:")

entero=875
print("\nEl tipo de dato de", entero, "es:\n", type(entero))

flotante=4.89
print("\nEl tipo de dato de", flotante, "es:\n", type(flotante))

texto="Now is better than never."
print("\nEl tipo de dato del texto:", texto, "es:\n", type(texto))

#En este caso, 1.32 se está ingesando como string
string="1.32"
print("\nEl tipo de dato de", string, "es:\n", type(string))

#He realizado una variación en este caso, supongo que el número
#que hay que analizar es un número complejo, por lo que he realizado
#la siguiente asignación en lugar de 5 + 8i:
complejo = 5 + 8j
print("\n¿El valor {} corresponde a un valor entero?".format(complejo))
if type(complejo)==int:
    print(f'{complejo} es un valor entero')
else:
    print(f'{complejo} NO es un valor entero')
    
texto = "Readability counts."
print("\n¿El texto {} corresponde a un string?".format(texto))
if type(texto)==str:
    print(f'{texto} corresponde a un string')
else:
    print(f"El texto: {texto} no corresponde a un string")

