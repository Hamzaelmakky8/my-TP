h=input("choisir une chaine de caractere :")
s=0
m=""
for i in h :
    if i==i :
        s=s+1
    m=m+i+str(s)
print(m)


if int(h)==m :
    print(f"{h} est nombre d'Armstrong ")
else:
    print(f"{h} n'est pas un nombre d'Armstrong ")