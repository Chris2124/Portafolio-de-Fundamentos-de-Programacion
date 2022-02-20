a=int(input("Introduce el año:"))
s=int(input("Introduce el salario:"))
if a<1:
    utilidad=s*0.05
elif (a>=1 and a<2):
    utilidad=s*0.07
elif (a>=2 and a<5):
    utilidad=s*.10
elif (a>=5 and a<10):
    utilidad=s*0.15
elif a>=10:
    utilidad=s*0.20
print("Su utilidad es de:", utilidad)