# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 08:21:40 2021

@author: Adrián Zambrano
"""

print("Programa que identifica el tipo de dato de un valor ingresado por el usuario, se realizarán cinco interacciones:")

iteraccion = ["Primera", "Segunda", "Tercera", "Cuarta", "Quinta"]

for i in iteraccion:
    print(f"\n{i} Interacción, ingrese un valor cualquiera:", end="")
    valor = input()
    try:
        print(f"Este tipo de dato en Python es:\n {type(int(valor))}")
        continue
    except:
        print(end="")
    try: 
        print(f"Este tipo de dato en Python es:\n {type(float(valor))}")
        continue
    except:
        print(end="")
    try:
        print(f"Este tipo de dato en Python es:\n {type(complex(valor))}")
        continue
    except:
        print(end="")
    try:
        print(f"Este tipo de dato en Python es:\n {type(bool(valor))}")
        continue
    except:
        print(end="")            
    try:
        print(f"Este tipo de dato en Python es:\n {type(valor)}")
        continue
    except:
        print(end="")
        
print("\n¡YA NO SE HARÁN MÁS INTERACCIONES!")
