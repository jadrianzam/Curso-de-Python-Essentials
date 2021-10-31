def programa2():
    
    print("Programa que identifica el tipo de dato de un valor ingresado por el usuario, se realizarán cinco interacciones:")
    
    iteraccion = ["Primera", "Segunda", "Tercera", "Cuarta", "Quinta"]
    
    """
    Si las entradas fueran tomadas solo desde input(), entonces todas serían
    de tipo str. He creído, por lo tanto, que sería interesante que el programa
    reconociera el tipo de dato que se está introduciendo, haciendo uso de la 
    detección de errores con try: y except:
    """
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
    
        if (valor == "True" or valor == "False"):
            print(f"Este tipo de dato en Python es:\n {type(bool(valor))}")
        else:
            print(f"Este tipo de dato en Python es, ya no hay más:\n {type(valor)}")
            
    print("\n¡YA NO SE HARÁN MÁS INTERACCIONES!")
