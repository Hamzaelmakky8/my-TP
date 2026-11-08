N=int(input("choisir la valeur de N :"))
s=0
if N>0 :
    for i in range(1,N+1) :
        s=s+(1/i)
    print("N=",s)
else:
    print("ERREUR !!")
