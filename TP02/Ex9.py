h=input("choisir un caractere : ")
if "A" <= h <= "Z" :
    print(f"{h} est un lettre majuscule ")
elif "a" <= h <= "z" :
    print(f"{h} est un lettre miniscule ")
else:
    print("Autre caractere ")
