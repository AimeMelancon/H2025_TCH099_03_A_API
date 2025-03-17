from flask import jsonify
from models import TraductionMatricule
from sqlalchemy import Select
from app import db

def getInstructions(module, matricule):
    # Requête SQL
    stmt = (
        Select(TraductionMatricule)
        .filter(TraductionMatricule.idMatricule == matricule, TraductionMatricule.nomModule == module)
    )

    # Exécution de la requête
    result = db.session.execute(stmt).scalars().first()

    if result is not None:
        return jsonify({"result": True}), 200
    else:
        return jsonify({"result": False}), 404
