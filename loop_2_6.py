n=5
contador_positivo=0
contador_negativo=0
contador_neutro=0
for i in range(n):
    num=int(input("Ingrese valor:"))
    if num>0:
        contador_positivo=+1
    elif num<0:
        contador_negativo=+1
    elif num==0:
        contador_neutro=+1
print("numeros positivos", contador_positivo)
print("numeros negativos", contador_negativo)
print("numeros neutros", contador_neutro)