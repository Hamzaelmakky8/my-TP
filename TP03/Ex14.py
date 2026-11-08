h=input("choisir une chaine de caractere :")
s=""
for i in h :
    if i in s :
        continue
    s=s+i
print(s)