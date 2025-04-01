import random
from models import TraductionCouleurs
from sqlalchemy import Select
from app import db
# dictionnaire

def patplayAlgo() :

    dic = {}
    # Toutes les formes + couleurs + positions
    couleurs = ["Rouge", "Bleu", "Jaune", "Vert"]
    formes = ["Triangle","Cercle","Carre","X"]
    positions = ["HG","HD","BG","BD"]

    # String de base (pour le dictionnaire)
    couleurForme = "couleur"
    formePosition = "forme"

    # Aléatoire pour la positions des couleurs par rapport à leur forme 
    listeNombre1 = random.sample(range(1,5), 4)
    listeCouleurs = [None,None,None,None]

    for i,value in enumerate(listeNombre1):
        listeCouleurs[value-1] = couleurs[i]

    # Met la clé/valeur pour le "couleur'Forme'" et chacune de leur couleur
    dic = {f"{couleurForme}{value}": listeCouleurs[i] for i,value in enumerate(formes)} 

    #---------------------------------------------
    #Placage pour les formes dans les différentes positions 

    listeNombre2 = random.sample(range(1,5), 4)
    listeFormes = [None,None,None,None]

    for i,value in enumerate(listeNombre2):
        listeFormes[value-1] = formes[i]

    dic.update({f"{formePosition}{value}": listeFormes[i] for i,value in enumerate(positions)})

    #-------------------------------------------------------------------------------------------------------------
    #Algorithme pour trouver la bonne suite pour patplay 

    Triangle = {"Jaune": 3, "Vert": 2, "Bleu": 1, "Rouge": 4} 
    Cercle = {"Jaune": 5, "Vert": 3, "Bleu": 2, "Rouge": 1}
    Carre = {"Jaune": 4, "Vert": 1, "Bleu": 3, "Rouge": 2}
    X = {"Jaune": 2, "Vert": 4, "Bleu": 5, "Rouge": 3}
    dicSeparer = list(dic.values())[0:4]

    def getSomme(): 
        somme = 0
        somme += Triangle[dicSeparer[0]]
        somme += Cercle[dicSeparer[1]]
        somme += Carre[dicSeparer[2]]
        somme += X[dicSeparer[3]]
        return somme

    #Triangle = 0 / Cercle = 1 / Carrée = 2 / X = 3 

    def getSolution():
        somme = getSomme()
        match somme :
            case 5:
                return "3021"
            case 7: 
                return "0132"
            case 9:
                return "1023"
            case 10: 
                return "1203"
            case 12:
                return "2310"
            case 14: 
                return "3102"
            case _: 
                return "0321"

    dic.update({"solution": getSolution()})

    # Fetch tous les mapping de couleur
    traductions = db.session.execute(
        Select(TraductionCouleurs.nomCouleur, TraductionCouleurs.hexCouleur)
    ).all()

    # Store dans un dictionnaire
    color_to_hex = {nom: hex_ for nom, hex_ in traductions}

    # Remplacer toutes les couleurs par leur couleur en hex, venant du dictionnaire créé précédemment
    for key in dic:
        if key.startswith("couleur"):
            original_color = dic[key]
            dic[key] = color_to_hex.get(original_color, original_color)  # fallback au nom original si pas de hex



    return dic