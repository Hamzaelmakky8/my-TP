n=int(input("choisir la valeur de n :"))
for i in range(2,n):
    for c in range(1,n) :
        if i%c==1 or i%c==i :
            print(i)
