#Faire un dictionnaire avec l'équivalent de la db (pour le module)                     FAIT
#Choisir aléatoirement pour créer les modules (tous sauf id_, solution)                FAIT
#Prendre ce qu'il y a dans le dictionnaire et trouver la solution avec l'algo          FAIT
#Transformer en JSON                                                                   FAIT
#Retourner le JSON                                                                     FAIT
#
# Dans une boucle for, tu met la clé (selon la table de numero) (i.e : couleurFils3), ensuite tu prend aléatoirement une couleur (choice) 

import random
from models import TraductionCouleurs
from sqlalchemy import Select
from app import db

def filsAlgo() :

    dic = {}
    # Couleurs possibles
    couleurs = ["Rouge", "Bleu", "Jaune", "Rose", "Blanc"]

    # String de base
    fils = "filsCouleur"

    # Nombre random entre 4-6
    nb = random.randint(4,6)

    # Liste triée avec un nombre aléatoire de nombres entre 1 et 6 choisis aléatoirement.
    liste = sorted(random.sample(range(1,7), nb))

    # Dictionnaire avec toutes les clés de 1 à 6
    dic = {"nbFils": nb}

    for i in liste:  # Boucle sur tous les nombres de 1 à 6
        dic[f"{fils}{i}"] = random.choice(couleurs)  # Assigne une couleur si dans la liste
        


    #---------------------------------------------------------------------------------------------------


    dicCouleurs = {"Rouge":0,"Bleu":0,"Jaune":0,"Rose":0,"Blanc":0, "":0}
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
                elif dicCouleurs["Rouge"] == 1 and dicCouleurs["Blanc"] > 0:
                    return 1
                elif dicCouleurs["Jaune"] == 0:
                    return 6
                else:
                    return 4 
                

    dic.update({"solution" : findSolution()})

    if dic["nbFils"] < 6 :
        if "filsCouleur1" not in dic : 
            dic["filsCouleur1"] = ""
        if "filsCouleur2" not in dic : 
            dic["filsCouleur2"] = ""
        if "filsCouleur3" not in dic : 
            dic["filsCouleur3"] = ""
        if "filsCouleur4" not in dic : 
            dic["filsCouleur4"] = ""
        if "filsCouleur5" not in dic : 
            dic["filsCouleur5"] = ""
        if "filsCouleur6" not in dic : 
            dic["filsCouleur6"] = ""

    

    # Fetch tous les mapping de couleur
    traductions = db.session.execute(
        Select(TraductionCouleurs.nomCouleur, TraductionCouleurs.hexCouleur)
    ).all()

    # Store dans un dictionnaire
    color_to_hex = {nom: hex_ for nom, hex_ in traductions}

    # Remplacer tous les filsCouleur par leur couleur en hex, venant du dictionnaire créé précédemment
    for key in dic:
        if key.startswith("filsCouleur"):
            original_color = dic[key]
            dic[key] = color_to_hex.get(original_color, original_color)  # fallback au nom original si pas de hex



    return dic

#-----------------------------------------------------------------------------------------------------------------