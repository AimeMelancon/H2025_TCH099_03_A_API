from flask import jsonify

from models import BipolarityInstructions1

from sqlalchemy import Select
from app import db
import random

def getbipolarityTable():
    # Requête SQL
    stmt = (
        Select(BipolarityInstructions1)
    )

    # Exécute la requête
    results = db.session.execute(stmt).all()

    # Retour
    if results:
        return [
            {
                "id_": data.id_, 
                "lettre": data.lettre, 
                "majuscule": data.majuscule,
                "minuscule": data.minuscule

            }
            for data in results
        ]

    else:       
        return "erreur"
    
def polariteAlgo() :
    liste_bipolariteTable = getbipolarityTable
    dic = {}
    # Lettre 1 / Lettre 2 / Lettre 3 / Lettre 4 / caseChoisie / couleur / solution 
    liste_lettres =  random.sample(range(1,27), 4)
    caseChoisie = random.randint(1,4)
    couleurChiffreChoisie = random.randint(1,2)
    couleurChoisie = ""
    solution = ""

    if (couleurChiffreChoisie == 1) :
        couleurChoisie = "Rouge"
    elif (couleurChiffreChoisie == 2) :
        couleurChoisie = "Bleu"

    dictLettre1 = liste_bipolariteTable[liste_lettres[0]-1]
    dictLettre2 = liste_bipolariteTable[liste_lettres[1]-1]
    dictLettre3 = liste_bipolariteTable[liste_lettres[2]-1]
    dictLettre4 = liste_bipolariteTable[liste_lettres[3]-1]

    dic["lettre1"] = dictLettre1.get("lettre")
    dic["lettre2"] = dictLettre2.get("lettre")
    dic["lettre3"] = dictLettre3.get("lettre")
    dic["lettre4"] = dictLettre4.get("lettre")
    dic["caseChosie"] = caseChoisie
    dic["couleur"] = couleurChoisie

    dicSolution = liste_bipolariteTable[liste_lettres[caseChoisie-1]]

    if (couleurChiffreChoisie == 1) :
        solution = dicSolution.get("majuscule")
    elif (couleurChiffreChoisie == 2) :
        solution = dicSolution.get("minuscule")

    dic["solution"] = solution

    return dic

    




    

