d=int(input("Introduce el día:"))
m=int(input("Introduce el mes:"))
if m<=0 or m>12 or d<=0 or d>31:
    print("fecha incorrecta")
elif (d>=22 and m==12) or (d<=20 and m==1):
    print("Capricornio")
elif (d>=21 and m==1) or (d<=19 and m==2):
    print("Acuario")
elif (d>=20 and m==2) or (d<=20 and m==3):
    print("Picis")
elif (d>=21 and m==3) or (d<=20 and m==4):
    print("Aries")
elif (d>=21 and m==4) or (d<=21 and m==5):
    print("Tauro")
elif (d>=22 and m==5) or (d<=21 and m==6):
    print("Geminis")
elif (d>=21 and m==6) or (d<=23 and m==7):
    print("Cancer")
elif (d>=24 and m==7) or (d<=23 and m==8):
    print("Leo")
elif (d>=24 and m==8) or (d<=23 and m==9):
    print("Virgo")
elif (d>=24 and m==9) or (d<=23 and m==10):
    print("Libra")
elif (d>=24 and m==10) or (d<=22 and m==11):
    print("Escorpio")
elif (d>=23 and m==11) or (d<=21 and m==12):
    print("Sagitario")