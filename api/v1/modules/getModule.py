from flask import jsonify
from sqlalchemy import Select
from models import Module
from app import db

def getModule(module):
    #Création de la requête à la db
    stmp =(
        Select(module.nom , module.schema)
    )
    #Permet d'avoir le résultat de la requête SQLite
     result = db.session.execute(stmt).scalars().first()
     
     if  result :
         return jsonify({"nom": result.nom, "schema" : result.schema}),200
    else:
        return jsonify({"error": "Module  non trouvé"}),404
    
