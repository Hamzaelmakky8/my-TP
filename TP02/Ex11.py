n=int(input("choisir la valeur de n :"))
if 0<=n<=6 :
    if n>=6 :
        print("aujourd'hui est samedi ")
    elif n>=5:
        print("aujourd'hui est vendredi ")
    elif n>=4 :
        print("aujourd'hui est jeudi")
    elif n>=3 :
        print("aujourd'hui est mercredi ")
    elif n>=2 :
        print("aujourd'hui est mardi ")
    elif n>=1 :
        print("aujourd'hui est lundi ")
    else :
        print("aujourd'hui est dimanche ")

else :
    print("ERREUER !!")