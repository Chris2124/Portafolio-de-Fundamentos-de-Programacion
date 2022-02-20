año=int(input("Ingrese el año:"))
if(año%400==0):
    print("Es un año bisiesto")
if(año%100==0):
    print("no Es un año bisiesto")
elif(año%4==0):
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")