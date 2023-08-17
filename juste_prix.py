# jeux du juste prix
from random import choice
print("nous allons jouer au jeux du juste prix")
rep=int(input("entrez un montant entre 1 et 1000: "))
cpt=0
nb=choice(list(range(1001)))
while rep!=nb and cpt<7:
    if rep<nb:
        rep=int(input("la valeur saisie est inférieur au nombre recherché,veuillez réessayer: "))
    else:
        rep=int(input("la valeur saisie est supérieur au nombre recherché,veuillez réessayer: "))
    cpt+=1
if cpt==7 and rep<nb:
    print("la dernière valeur saisie est inférieure au nombre recherché")
else:
    print("la dernière valeur saisie est supérieure au nombre recherché")

print(f"vous avez déja écoulé {cpt} tentatives")
answer=input("voulez vous un indice? ")
if answer.lower()=="oui":
    if(nb%2==0):
        print("en réalité le nombre à trouver est pair")
    else:
        print("en réalité le nombre à trouver est impair")
rep=int(input("maintenant veuillez réesayer à nouveau: "))
while rep!=nb:
    if rep<nb:
        rep=int(input("la valeur saisie est inférieur au nombre recherché,veuillez réessayer: "))
    else:
        rep=int(input("la valeur saisie est supérieur au nombre recherché,veuillez réessayer: "))
    cpt+=1
if cpt>7:
    print("bravo,félicitations,vous avez finallement trouvé le juste prix après {} tentatives".format(cpt))
else:
    print("bravo,félicitations,vous avez trouvé le juste prix après {} tentatives".format(cpt))