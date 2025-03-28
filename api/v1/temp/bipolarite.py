from flask import jsonify
from models import Bipolarite
from sqlalchemy import Select
from app import db

def getBipolarite():


    # Requête SQL
    stmt = Select(Bipolarite)

    # Exécute la requête
    results = db.session.execute(stmt).scalars().all()

    # Retour
    if results:
        return jsonify([
            {
                "id_": bipolarite.id_,
                "lettre1": bipolarite.lettre1,
                "lettre2": bipolarite.lettre2,
                "lettre3": bipolarite.lettre3,
                "lettre4": bipolarite.lettre4,
                "caseChoisie": bipolarite.caseChoisie,
                "couleur": bipolarite.couleur,
                "solution": bipolarite.solution
            }
            for bipolarite in results
        ]), 200
    else:
        return jsonify({"error": "Aucun Bipolarité trouvé"}), 404