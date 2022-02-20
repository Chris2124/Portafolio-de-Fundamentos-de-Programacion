d=int(input("Introduce el día:"))
m=int(input("Introduce el mes:"))
a=int(input("Introduce el año:"))
if m<=0 or m>12 or d<=0 or d>31 or a<=0:
    print("fecha invalida")
elif m in (1, 3, 5, 7, 8, 10, 12):
    if d==31 and m==12:
        a=a+1
        m=1
        d=1
    elif d==31 and m!=12:
        m=m+1
        d=1
    else:
        d=d+1        
    print("La fecha siguiente es:", d,"/", m,"/", a)
elif m in (4, 6, 9, 11) and d<=30:
    if d==30:
        m=m+1
        d=1
    else:
        d=d+1
    print("La fecha siguiente es:", d,"/", m,"/", a)
elif m==2 and d<=28:
    if d==28:
        m=m+1
        d=1
    print("La fecha siguiente es:", d,"/", m,"/", a)
else:
    print("fecha invalida")

