n=int(input("choisir la valeur de n :"))
if n>0 :
    s=0
    m=0
    for i in str(n) :
        s=s+1
        p=int(i)**s
        m=m+p
    print("m=",m)







