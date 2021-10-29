# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 08:59:06 2021

@author: Adrián Zambrano
"""
def delMenu1():
    print("Elija una opción:")
    print("1) Demostración del cálculo de valores altos y bajos en diccionarios.")
    print("2) Salir.\n")
    opcion = input("Seleccione una opcion: ")
    return opcion

def delMenu2():
    print("\nElija un diccionario para la demostración:")
    print("1) {Raul:34,Paula:19,Jorge:43,Richard:10,Diana:3,Isabel:76,Gustavo:12,Diego:37}")
    print("2) {tplA:(4,-12,56,-34,98,102),tplB:(9,0,1,10,-3,14),tlpC:(87,12,56,987,-61)}")
    print("3) {val1:-12.5,val2:12.5,val3:83,val4:2.1,val5:23,val6:100,val7:13.4,val8:92}")
    print("4) {lst1:[4,6,-12,56,-9,5.7,33,100],lst2:[9,0,81,-2,-56,],lst3:[12,31,87,1,0,4,-11]}\n")
    opcion = input("Seleccione una opcion: ")
    return opcion

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
    opcion = delMenu1()
    if opcion != "1" and opcion != "2":
        print("\n\nSu selección fue inválida. Realice una nueva selección.\n")
        continue
    elif opcion == "1":
        opcion = int(delMenu2())
        while True:
            if opcion not in [1, 2, 3, 4]:
                print("\n\nSu selección fue inválida. Realice una nueva selección.\n")
                input("Presione ENTER para continuar\n\n")
                continue
            else:
                while True:
                    altos=int(input("Digite el número de valores altos que desea mostrar: "))
                    bajos=int(input("Digite el número de valores bajos que desea mostrar: "))
 
                    #Obtengo una lista de los valores del diccionario elegido. Estos
                    #podrían ser números, tuplas o listas
                    listaValores = list(lista[opcion -1].values())
                    print("listaValores = ", listaValores)
                    
                    #Cada valor debería transformarlo a una lista para ir añadiendolos
                    #a la lista total
                    longDict = len(lista[opcion-1])

                    listaTotal = []
                    for i in range(0,longDict):
                        try:
                            listaTotal.extend(list(listaValores[i]))
                        except:
                            listaTotal = listaValores    
                    print("listaTotal =", listaTotal)
                    longlistaTotal = len(listaTotal)
                    
                    print("Longitud de la lista total: ", longDict)
                    if altos<=longlistaTotal and bajos<=longlistaTotal:
                        lista2=sorted(listaTotal)
                        print("lista2 = ", lista2)
                        print("Valores bajos en formato lista: ", lista2[0:bajos])
                        print("Valores altos en formato lista: ", lista2[-altos:])
                        print("Valores bajos en formato tupla: ", tuple(lista2[0:bajos]))
                        print("Valores altos en formato tupla: ", tuple(lista2[-altos:]))
                        input("\nPresione ENTER para continuar ...")
                        break
                    else:
                        print("La cantidad de valores altos o bajos no puede ser mayor que el tamaño de los diccionarios")
                        continue
            break
    else:
        break
                























