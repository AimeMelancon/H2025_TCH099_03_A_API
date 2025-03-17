from flask import jsonify
from sqlalchemy import Select
from models import Matricule, Module
from app import db

def verifyMatricule(module, matricule):
    """Vérifie si le nom du module est présent, si le matricule existe et s'ils sont liés

    Route associée: '/api/v1/<module>/<matricule>', méthodes: GET

    Paramètres: 
      module (str): Le nom du module
      matricule (str): Le matricule lui-même, qui est un string d'une longueur de 6 charactères.

    Retour:
      Si le module et matricule spécifiés existe existe dans la base de données, et s'ils sont liés:
        {"result": true}  
        Réponse HTTP: 200 OK

      Sinon:
        {"result": false} Sinon.
        Réponse HTTP: 404 Not Found
    """

    # Requête SQL
    stmt = (
        Select(Matricule)
        .join(Module, Matricule.module_id == Module.id_)
        .filter(Module.nom == module, Matricule.numero == matricule)
    )

    # Exécution de la requête
    result = db.session.execute(stmt).scalars().first()

    # Retour (avec la bonne réponse HTTP)
    if result is not None:
        return jsonify({"result": True}), 200
    else:
        return jsonify({"result": False}), 404



        
