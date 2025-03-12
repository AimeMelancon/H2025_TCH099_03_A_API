from flask import jsonify
from models import Niveau
from sqlalchemy import Select
from app import db

def getNiveaux():
    """Récupère tous les niveaux présents dans la base de données.

    
    Route associée: '/api/v1/niveaux', méthodes: GET

    Retour:
      S'il y a des niveaux:
        Une liste de dictionnaires (hashmaps)  tel que:
        [{"color" : (string), "description": (string), "difficulty": (string), "duration": (integer), "id": (integer), "nom": (string)}, ...]
        Réponse HTTP: 200 OK

      Sinon:
        {"error": "Instruction non trouvée."}
        Réponse HTTP: 404 Not Found
    """

    # Requête SQL
    stmt = (
        Select(Niveau)
    )

    # Exécute la requête
    liste = db.session.execute(stmt).scalars().all()

    # Retour
    if liste:
        return jsonify([{"id": niveau.id_, 
                         "nom": niveau.nom, 
                         "description": niveau.description, 
                         "duration": niveau.duration, 
                         "difficulty": niveau.difficulty, 
                         "color": niveau.color}
                        for niveau in liste]), 200
    else:       
        return jsonify({"error": "Aucun niveau trouvé"}), 404
