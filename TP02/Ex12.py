a=int(input("choisir la valeur de a :"))
b=int(input("choisir la valeur de b"))
c=int(input("choisir la valeur de c "))
if a==0 :
    if b==0 :
        if c==0 :
            print("l'ensemble de solutions de l'equation est ℝ ")
        else :
            print("l'ensemble de solutions de l'equation est l'ensemble vide ")
    else :
        x=-c/b
        print(f"la solution de l'equationest {x}")
else :
    D=b*b-4*a*c
    if D==0 :
        x=-b/(2*a)
        print(f"la solution de l'equation est {x}")
    elif D<0 :
        print("l'equation n'admit pas de solution dans l'ensemble ℝ")
    else:
        x1=(-b-(D)**(1/2)/(2*a))
        x2=(-b+(D)**(1/2)/(2*a))
        print(f"les solution de l'equation sont : {x1} et {x2}")


