N=int(input("choisir la valeur de N : "))
if N>0 :
    for c in range(1,N+1) :
        s=0
        for i in range(1,c) :
            if c%i==0 :
                s=s+i
        if s==c :
            print(s)
elif N<0 : 
    print("ERREUR !!")
else:
    print("0")