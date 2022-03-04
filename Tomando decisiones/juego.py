import random

op = -1
eleccion = -1 
empates=0
ganados=0
perdidos=0

def menu ():
    print("<1> jugar")
    print("<2> resultados")
    print("<3> salir")    
while op != 0:
        menu ()
        op = int(input("ingrese una opcion: "))
        if op == 1:
            while eleccion != 0:
                print("<1> piedra")
                print("<2> papel")
                print("<3> tijera")
                print('<0> regresar')
                eleccion = int(input("ingrese un numero al juego: "))
                if eleccion == 0:
                    menu()
                num = random.randint(1,3)
                
                if eleccion==1:
                    if num==2:
                        print ("pierdo", 'piedra', "vs", 'papel')
                        perdidos+=1
                    elif num ==3:
                        print ("gano", 'piedra', "vs",'tijera')
                        ganados+=1
                    elif eleccion== num:
                        print ("Empate", "piedra", "vs", "piedra")
                        empates+=1
                
                if eleccion==2:
                    if num==1:
                        print ("gano", 'papel', "vs", 'piedra')
                        ganados+=1
                    elif num==3:
                        print ("pierdo", 'papel', "vs", 'tijera')
                        perdidos+=1
                    elif eleccion ==num:
                        print ("Empate", 'papel', "vs", 'papel')
                        empates+=1

                
                if eleccion==3:
                    if num==1:
                        print ("pierdo", 'tijera', "vs", 'piedra')
                        perdidos+=1
                    elif num==2:
                        print ("gano", 'tijera', "vs", 'papel')
                        ganados=+1
                    elif eleccion ==num:
                        print ("Empate", 'tijera', "vs", 'tijera')
                        empates+=1
                    else:
                        print("ingrese una opcion correcta")
        elif op == 2:
            print("ganados: ",ganados)
            print("perdidos: ", perdidos)
            print("empatados: ",empates)
        elif op == 3:
            quit()
        else:
            print("ingrese una opcion correcta")