n=int(input("choisir la valeur de n :"))
x=int(input("choisir la valeur de x :"))
if n>x :
    x=int(input("choisir la valeur de x :"))
    if n>x:
        x=int(input("choisir la valeur de x :"))
        if n>x :
            print("le nombre la plus grand est :",n)
        else :
            print("le nombre la plus grand est :",x)
    else :
        n=int(input("choisir la valeur de n :"))
        if n>x :
            print("le nombre la plus grand est :",n)
        else:
            print("le nombre la plus grand est :",x)
else:
    n=int(input("choisir la valeur de n :"))
    if x>n :
        n=int(input("choisir la valeur de n :"))
        if x>n :
            print("le nombre la plus grand est :",x)
        else:
            print("le nombre la plus grand est :",n)
    else:
        x=int(input("choisir la valeur de x :"))
        if n>x :
            print("le nombre la plus grand est :",n)
        else:
            print("le nombre la plus grand est :",x)
