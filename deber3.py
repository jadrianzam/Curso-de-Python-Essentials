import funProg5

def programa5():
    #Definiendo los diccionarios:
    dic1={"Raul":34,"Paula":19,"Jorge":43,"Richard":10,"Diana":3,"Isabel":76,"Gustavo":12,"Diego":37}
    dic2={"tplA":(4,-12,56,-34,98,102),"tplB":(9,0,1,10,-3,14),"tlpC":(87,12,56,987,-61)}
    dic3={"val1":-12.5,"val2":12.5,"val3":83,"val4":2.1,"val5":23,"val6":100,"val7":13.4,"val8":92}
    dic4={"lst1":[4,6,-12,56,-9,5.7,33,100],"lst2":[9,0,81,-2,-56,],"lst3":[12,31,87,1,0,4,-11]}
    
    lista=[]
    lista.append(dic1)
    lista.append(dic2)
    lista.append(dic3)
    lista.append(dic4)
    
    
    while True:
        opcion = funProg5.delMenu1()
        if opcion != "1" and opcion != "2":
            print("\n\nSu selección fue inválida. Realice una nueva selección.\n")
            continue
        elif opcion == "1":
            opcion = int(funProg5.delMenu2())
            while True:
                if opcion not in [1, 2, 3, 4]:
                    print("\n\nSu selección fue inválida. Realice una nueva selección.\n")
                    input("Presione ENTER para continuar\n\n")
                    continue
                else:
                    funProg5.altosBajos(lista, opcion)
                break
        else:
            break









