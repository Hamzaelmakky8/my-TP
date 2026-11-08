n=int(input("saisir la valeur de n :"))
s=0
if n>0:
    for i in range(1,n) :
        if n%i==0 :
            s=s+i
    if n==s :
        print(f"{n} est un nombre parfait ")   
    else:
        print(f"{n} n'est pas un nombre parfait ")
else :
    print("ERREUR!!!")