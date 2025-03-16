from flask import jsonify
from models import Niveau, TraductionCouleurs
from sqlalchemy import Select
from app import db

def getNiveaux():
    """Récupère tous les niveaux présents dans la base de données.

    
    Route associée: '/api/v1/niveaux', méthodes: GET

    Retour:
      S'il y a des niveaux:
        Une liste de dictionnaires (hashmaps)  tel que:
        [{"color" : (string), "description": (string), [...] ]
        Réponse HTTP: 200 OK

      Sinon:
        {"error": "Instruction non trouvée."}
        Réponse HTTP: 404 Not Found
    """

    # Requête SQL avec JOIN
    stmt = (
        Select(Niveau, TraductionCouleurs.hexCouleur)
        .join(TraductionCouleurs, Niveau.color == TraductionCouleurs.nomCouleur)
    )

    # Exécute la requête
    results = db.session.execute(stmt).all()

    # Retour
    if results:
        return jsonify([
            {
                "id": niveau.id_, 
                "nom": niveau.nom, 
                "description": niveau.description, 
                "duration": niveau.duration, 
                "difficulty": niveau.difficulty, 
                "color": hex_code,  # Utilisation du code hex au lieu du nom de la couleur
                "nbEvent": niveau.nbEvent
            }
            for niveau, hex_code in results
        ]), 200
    else:       
        return jsonify({"error": "Aucun niveau trouvé"}), 404
