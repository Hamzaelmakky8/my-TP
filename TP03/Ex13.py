n=int(input("taper un nombre n :"))
if n<=1 :
    print("ERREUR !!")
else :
    for c in range(2,n+1) :
        s=0
        for i in range(1,c+1) :
            if c%i==0 :
                s=s+1
            if s==2 :
                print(c)
    