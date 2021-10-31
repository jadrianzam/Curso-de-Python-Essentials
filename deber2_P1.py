def programa3() :
    
    #He considerado que hubo un error al usar [] en lugar de () para una tupla
    #Por esta razón escribo Datos_2021 de esta forma:
    Datos_2021 = (15, 20, 3,91,4, 5, 6, 7,100,91,110,900,21,33,32, 2, 4,8,10,13,13,16,15,1302)
    
    #Puesto que usaré el método append, necesito trabajar con una lista
    lista_datos = list(Datos_2021)
    
    pares = []
    impares = []
    atipicos = []
    
    for n in lista_datos:
        if n%2 == 0:
            pares.append(n)
        else:
            impares.append(n)       
        if n > 90: # Consideraré atípicos a los números mayores a 90
            atipicos.append(n)
    
            
    print("Números pares:")
    print(pares)
    
    print("Números impares:")
    print(impares)
    
    print("Números atípicos:")
    print(atipicos)
