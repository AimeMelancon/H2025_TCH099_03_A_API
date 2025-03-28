from flask import jsonify
from models import Bipolarity
from sqlalchemy import Select
from app import db

def getBipolarite():


    # Requête SQL
    stmt = Select(Bipolarity)

    # Exécute la requête
    results = db.session.execute(stmt).scalars().all()

    # Retour
    if results:
        return jsonify([
            {
                "id_": bipolarity.id_,
                "lettre1": bipolarity.lettre1,
                "lettre2": bipolarity.lettre2,
                "lettre3": bipolarity.lettre3,
                "lettre4": bipolarity.lettre4,
                "caseChoisie": bipolarity.caseChoisie,
                "couleur": bipolarity.couleur,
                "solution": bipolarity.solution
            }
            for bipolarity in results
        ]), 200
    else:
        return jsonify({"error": "Aucun Bipolarité trouvé"}), 404