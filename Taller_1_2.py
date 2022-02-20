n=10
sum=0
baja=9999
for i in range(n):
    nota=int(input("Ingrese nota " + str(i+1) + ":"))
    sum=sum+nota
    if nota<baja:
        baja=nota
promedio=sum/n
print("Promedio:", promedio, "Nota mas bajas:", baja)