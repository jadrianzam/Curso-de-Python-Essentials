# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 07:35:46 2021

Desarrollar un programa que permita validar la contraseña introducida por un 
usuario con las siguientes comprobaciones:
- Debe contener al menos una letra minúscula entre las letras: 
    a,b,c,d,e,f,g,h,i,j.
- Debe contener al menos una letra mayúscula entre las letras: 
    K,L,M,N,O,P,Q,R,S,T.
- Debe contener al menos un número entre 
    0 y 9.
- Debe contener un símbolo especial entre: 
    $,%,*,@
- Tamaño mínimo de 5 caracteres y máximo de 15.

Se debe solicitar la contraseña al usuario, así como informarle sobre estos 
requisitos para su contraseña, una vez validada mostrar un mensaje al usuario informándole al respecto.

@author: Adrián Zambrano
"""

# Definiendo las restricciones:
minusculas = ['a','b','c','d','e','f','g','h','i','j']
mayusculas = ['K','L','M','N','O','P','Q','R','S','T']
especiales = ['$','%','*','@']
numeros = ['0','1','2','3','4','5','6','7','8','9']


while True:
    #Pido datos:
    password=input("Ingrese una contraseña: ")
    longitud = len(password)

    if (longitud < 5 or longitud > 15):
        print("La constraseña debe tener entre 5 y 15 caracteres.")
        print(f"Su contraseña tiene {longitud} caracteres.")
        continue
    
    # Para verificar minúsculas:   
    contador=0
    for c in password:
        if c in minusculas:
            contador += 1
    if contador < 1:
        print("El password debe contener al menos una de estas minúsculas:")
        print(minusculas)
        continue
    
    # Para verificar mayúsculas:   
    contador=0
    for c in password:
        if c in mayusculas:
            contador += 1
    if contador < 1:
        print("El password debe contener al menos una de estas minúsculas:")
        print(mayusculas)
        continue
    
    # Para verificar caracteres especiales:   
    contador=0
    for c in password:
        if c in especiales:
            contador += 1
    if contador < 1:
        print("El password debe contener al menos una de estas minúsculas:")
        print(especiales)
        continue
    
    # Para verificar números:   
    contador=0
    for c in password:
        if c in numeros:
            contador += 1
    if contador < 1:
        print("El password debe contener al menos una de estas minúsculas:")
        print(numeros)
        continue
    
    print("Su contraseña ha sido aceptada")
    break

















