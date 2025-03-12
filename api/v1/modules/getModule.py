from flask import jsonify
from sqlalchemy import Select
from models import Module
from app import db

def getModule(module):
    #Création de la requête à la db
    stmt =(
        Select(Module)
        .filter(Module.nom ==module)
    )
    #Permet d'avoir le résultat de la requête SQLite
    result = db.session.execute(stmt).scalars().first()
    print(result)
    #Traitement du résultat 
    if result:
       #TODO:Si on peut on va faire en sorte que c'est la requête qui se charge de sélectionner les paramètres souhaités!
        return jsonify({"nom": result.nom, "schema": result.schema}), 200
    else:
        return jsonify({"error": "Module  non trouvé"}),404
    
