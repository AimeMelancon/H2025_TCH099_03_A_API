from flask import jsonify
from sqlalchemy import Select
from models import Module
from app import db

def getModule(module):
    """Récupère un module par son nom.

    
    Route associée: '/api/v1/niveaux', méthodes: GET

    Retour:
      Si le module existe:
        {"schema" : (string), "description": (string)}
        Réponse HTTP: 200 OK

      Sinon:
        {"error": "Module non trouvé"}
        Réponse HTTP: 404 Not Found
    """
    #Création de la requête à la db
    stmt =(
        Select(Module)
        .filter(Module.nom ==module)
    )
    #Permet d'avoir le résultat de la requête SQLite
    result = db.session.execute(stmt).scalars().first()

    #Traitement du résultat 
    if result:
       #TODO:Si on peut on va faire en sorte que c'est la requête qui se charge de sélectionner les paramètres souhaités!
        return jsonify({"nom": result.nom, "schema": result.schema}), 200
    else:
        return jsonify({"error": "Module non trouvé"}), 404