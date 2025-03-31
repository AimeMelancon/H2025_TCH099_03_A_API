from flask import jsonify

from models import LightsInstructions1

from sqlalchemy import Select
from app import db
import random

def getLightsTable():
    # Requête SQL avec JOIN
    stmt = (
        Select(LightsInstructions1)
    )

    # Exécute la requête
    results = db.session.execute(stmt).all()

    # Retour
    if results:
        return [
            {
                "id_": data.id_, 
                "lumiers": data.nom, 
                "leviers": data.description, 
            
            }
            for data in results
        ]

    else:       
        return "erreur"


def lightsAlgo():
    liste = getLightsTable()

    LENGTH = len(liste) 
    choix = random.randint(1,LENGTH)    

    dic = liste[LENGTH-1]  
    dic.pop("id_")

    dic["solution"] = dic["leviers"]
    dic.pop("leviers")

    return dic


