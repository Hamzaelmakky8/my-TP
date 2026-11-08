h=str(input("choisir une chaine de caractere :"))
v=input("choisir une caractere :")
s=0
for i in h :
    if v==i :
        s=s+1
print(f"le nombre d’occurrences {h} dans la chaîne est : {s}")
