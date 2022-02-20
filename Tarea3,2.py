num1, num2, num3=int(input("Ingrese un valor:")), int(input("Ingrese un valor:")), int(input("Ingrese un valor:"))
if((num1>num2) and (num1>num3)):
    print("El mayor valor es:", num1)
elif((num2>num1) and (num2>num3)):
    print("El mayor valor es:", num2)
elif((num3>num1) and (num3>num2)):
    print("El mayor valor es:", num3)
elif(num1==num2==num3):
    print("Los valores son iguales")
elif((num1==num2)or(num1==num3)):
    print("El mayor valor es:", num1)
elif(num2==num3):
    print("El mayor valor es:", num2)