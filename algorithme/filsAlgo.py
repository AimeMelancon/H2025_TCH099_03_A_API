def filsAlgo(): pass

#Faire un dictionnaire avec l'équivalent de la db (pour le module)                     FAIT
#Choisir aléatoirement pour créer les modules (tous sauf id_, solution)                FAIT
#Prendre ce qu'il y a dans le dictionnaire et trouver la solution avec l'algo          A FAIRE
#Transformer en JSON                                                                   A FAIRE
#Retourner le JSON                                                                     A FAIRE
#
# Dans une boucle for, tu met la clé (selon la table de numero) (i.e : couleurFils3), ensuite tu prend aléatoirement une couleur (choice) 

import random
# dictionnaire
dic = {}
# Couleurs possibles
couleurs = ["Rouge", "Bleu", "Jaune", "Rose", "Blanc"]

# String de base
fils = "filsCouleur"

# Nombre random entre 4-6
nb = random.randint(4,6)

# Liste triée avec un nombre aléatoire de nombres entre 1 et 6 choisis aléatoirement.
liste = sorted(random.sample(range(1,7), nb))


# Dictionnaire (trié) avec tous les fils
dic = {f"{fils}{i}": random.choice(couleurs) for i in liste}


# Rajouter nbFils au début
# l'opérateur ** unpack le dictionnaire (retourne le reste du dict)
dic = {"nbFils": nb, **dic}


#---------------------------------------------------------------------------------------------------


dicCouleurs = {"Rouge":0,"Bleu":0,"Jaune":0,"Rose":0,"Blanc":0}
listeValeur = list(dic.values())

def findLastColor(color):
    number = 0
    for i, value in enumerate(listeValeur):
        if value == color:
            number = i
    return number


for key, value in list(dic.items())[1:]:
    dicCouleurs[value] += 1

def findSolution():
    match dic.get("nbFils"):
        case 4:
            if dicCouleurs["Rouge"] > 1:
                return 4
            elif listeValeur[4] == "Jaune":
                return 1
            elif dicCouleurs["Bleu"] == 1:
                return 1
            else:
                return 2
        case 5:
            if listeValeur[5] == "Rose":
                return 1
            elif dicCouleurs["Jaune"] == 2:
                return 4
            elif dicCouleurs["Blanc"] == 0:
                return 2
            else:
                return 3
        case 6:
            if dicCouleurs["Rose"] > 2:
                return findLastColor("Rose")
            elif dicCouleurs["Rouge"] == 1 and dicCouleurs["Blanc"] == 0:
                return 1
            elif dicCouleurs["Jaune"] == 0:
                return 6
            else:
                return 4 
            

dic.update({"solution" : findSolution()})

print(dic)

#-----------------------------------------------------------------------------------------------------------------