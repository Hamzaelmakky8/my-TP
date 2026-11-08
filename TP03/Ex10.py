n=int(input("choisir la valeur de n : "))
s=0
for i in str(n) :
    p=1
    for c in range(1,int(i)+1) :
        p=p*c
    s=s+p
if n==s :
    print(f"{n} est un nombre fort ")
else:
    print(f"{n} n'est pas un nombre fort ")
