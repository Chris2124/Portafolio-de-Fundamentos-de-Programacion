num1, num2, num3, num4=int(input("Ingrese un valor:")), int(input("Ingrese un valor:")), int(input("Ingrese un valor:")), int(input("Ingrese un valor:"))
if(num1<num2):
    num1, num2=num2, num1
if(num1<num3):
    num1, num3=num3, num1
if(num1<num4):
    num1, num4=num4, num1
if(num2<num3):
    num2, num3=num3, num2
if(num2<num4):
    num2, num4=num4, num2
if(num3<num4):
    num3, num4=num4, num3
print(num1)
print(num2)
print(num3)
print(num4)
