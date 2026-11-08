A=str(input("le nom de premier personne est :"))
B=str(input("le nom de deuxieme personne est :"))
C=str(input("le nom de troisieme personne est :"))
a=float(input("l'age de premier personne est :"))
b=float(input("l'age de deuxieme personne est "))
c=float(input("l'age de troisieme personne est :"))

if a>b :
    if b>c :
        print("la personne la plus grand est :",A)
    elif a>c :
        print("la personne la plus grand est :",A)
    else:
        print("la personne la plus grand est :",C)
elif b>c :
    print("la personne la plus grand est :",B)
else :
    print("la personne la plus grand est :",C)

