from flask import jsonify
from models import Wires
from sqlalchemy import Select
from app import db

def getFils():


    # Requête SQL
    stmt = Select(Wires)

    # Exécute la requête
    results = db.session.execute(stmt).scalars().all()

    # Retour
    if results:
        return jsonify([
            {
                "id_": wire.id_,
                "nbFils": wire.nbFils,
                "couleurFil1": wire.couleurFil1,
                "couleurFil2": wire.couleurFil2,
                "couleurFil3": wire.couleurFil3,
                "couleurFil4": wire.couleurFil4,
                "couleurFil5": wire.couleurFil5,
                "couleurFil6": wire.couleurFil6,
                "solution": wire.solution
            }
            for wire in results
        ]), 200
    else:
        return jsonify({"error": "Aucun fil trouvé"}), 404