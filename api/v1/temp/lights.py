from flask import jsonify
from models import Lights
from sqlalchemy import Select
from app import db

def getLights():


    # Requête SQL
    stmt = Select(Lights)

    # Exécute la requête
    results = db.session.execute(stmt).scalars().all()

    # Retour
    if results:
        return jsonify([
            {
                "id_": light.id_,
                "lumiere": light.lumiere,
                "solution": light.solution
            }
            for light in results
        ]), 200
    else:
        return jsonify({"error": "Aucune lumière trouvée"}), 404