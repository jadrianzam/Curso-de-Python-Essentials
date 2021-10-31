# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 07:08:24 2021

@author: Usuario
"""
import deber1_P1, deber1_P2, deber2_P1, deber2_P2, deber3

while True:
    print("Menú de programas:\n")
    print("\
    1. Programa que muestra los distintos tipos de datos que maneja Python\n\
    2. Programa que pide un dato y muestra de qué tipo es\n\
    3. Programa que separa los elementos de una tupla en pares, impares y atípicos\n\
    4. Programa que pide una contraseña que cumpla con ciertas restricciones\n\
    5. Programa que muestra valores bajos y altos de una lista\n\
    6. Salir\n")
    opcion = input("Escoja el programa que desea ejecutar: ")
    
    if opcion == "1":
        #exec(open("deber1_P1.py").read())
        deber1_P1.programa1()
    elif opcion == "2":
        deber1_P2.programa2()
    elif opcion == "3":
        deber2_P1.programa3()
    elif opcion == "4":
        deber2_P2.programa4()
    elif opcion == "5":
        try:
            deber3.programa5()
        except:
            print("Lo siento, hubo un error en el programa.") 
            print("Seguramente introdujo un caracter no válido.")
        else:
            print("Excelente opción.")
        finally:
            print("Puede seguir utilizando el programa.")
    elif opcion == "6":
        print("\nFin del programa")
        break
    else:
        print("Su selección fue incorrecta.\nInténtelo nuevamente.")
        
    input("Presione una tecla para continuar ...")
            