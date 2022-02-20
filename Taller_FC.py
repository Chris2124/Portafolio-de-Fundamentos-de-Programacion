d=int(input("Introduce el día:"))
m=int(input("Introduce el mes:"))
a=int(input("Introduce el año:"))
if m<=0 or m>12 or d<=0 or d>31 or a<=0:
    print("fecha incorrecta")
elif m==4 or m==6 or m==9 or m==11:
    if d>30:
        print("fecha incorrecta")
elif m==2:
    if a%400==0 or a%4==0 and d>29:
        print("fecha incorrecta") 
    elif d<=29:
         print("La fecha es correcta")
    elif a%100==0 and d>28:
        print("fecha incorrecta")
    elif d<=28:
         print("La fecha es correcta")
    else:
        if d>28:
            print("fecha incorrecta")
        elif d<=28:
         print("La fecha es correcta")  
else:
    print("La fecha es correcta")