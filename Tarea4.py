num=int(input("Ingrese la temperatura:"))
if(num<0):
    print("El agua esta en estado solido")
if(0<=num<100):
    print("El agua esta en estado liquido")
if(num>100):
    print("El agua esta en estado gaseoso")