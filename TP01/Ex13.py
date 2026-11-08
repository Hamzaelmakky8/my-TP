a=float(input("saisir la quantite achetee :"))
b=float(input("saisir le prix unitaire :"))
prixtotal=a*b
mr=prixtotal*0.15
pf=prixtotal-mr
print(f"le prix totale avant la reduction est : {prixtotal}")
print(f"le montant de la reduction est : {mr}")
print(f"le prix final a payer est :{pf}")
