h=str(input("choisir une chaine de caractere :"))
s=""
m=(h.lower())
for i in m :
    s=i+s
if s==m :
    print(f"{h} est un palindrome")
else :
    print(f"{h} n'est pas un palindrome")