op=-1
num1=0
num2=0
while op != 0:
    print("<1> Suma")
    print("<2> Resta")
    print("<3> Multiplicación")
    print("<4> División")
    print("<0> Salir")
    op=int(input("Ingrese opción: "))
    if op != 0:
        num1=int(input("Ingrese valor 1: "))
        num2=int(input("Ingrese valor 2: "))
    elif op==1:
        print("Suma: ", num1+num2)
    elif op==2:
        print("Resta: ", num1-num2)
    elif op==3:
        print("Multiplicación: ", num1*num2)
    elif op==4:
        print("División: ", num1/num2)
    else:
        print("No existe la opción")
