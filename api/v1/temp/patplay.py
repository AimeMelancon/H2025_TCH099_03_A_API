from flask import jsonify
from models import Fils
from sqlalchemy import Select
from app import db

def getPatplay():


    # Requête SQL
    stmt = Select(Fils)

    # Exécute la requête
    results = db.session.execute(stmt).scalars().all()

    # Retour
    if results:
        return jsonify([
            {
                "id_": fils.id_,
                "nbFils": fils.nbFils,
                "couleurFil1": fils.couleurFil1,
                "couleurFil2": fils.couleurFil2,
                "couleurFil3": fils.couleurFil3,
                "couleurFil4": fils.couleurFil4,
                "couleurFil5": fils.couleurFil5,
                "couleurFil6": fils.couleurFil6,
                "solution": fils.solution
            }
            for fils in results
        ]), 200
    else:
        return jsonify({"error": "Aucun fil trouvé"}), 404