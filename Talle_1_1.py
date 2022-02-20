n=int(input("Introduce la cantidad de numeros:"))
suma=0
for i in range(n):
    nota=int(input("Ingrese nota " + str(i+1) + ":"))
    suma+=nota
promedio=suma/n
print("Suma:", suma, "Promedio:", promedio)
