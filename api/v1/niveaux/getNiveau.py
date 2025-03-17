from flask import jsonify
from models import Niveau, TraductionCouleurs
from sqlalchemy import Select
from app import db

def getNiveau(niveau):
    """Récupère le niveau spécifié en paramètre de la base de données.

    
    Route associée: '/api/v1/niveau/<int:niveau>', méthodes: GET

    Paramètres:
      niveau (int): le id du niveau.

    Retour:
      Si le niveau est présent:
        Un dictionnaire (hashmap)  tel que:
        [{"color" : (string), "description": (string), [...] ]
        Réponse HTTP: 200 OK

      Sinon:
        {"error": "Niveau non trouvé"}
        Réponse HTTP: 404 Not Found
    """

    # Requête SQL
    stmt = (
        Select(Niveau, TraductionCouleurs.hexCouleur)
        .join(TraductionCouleurs, Niveau.color == TraductionCouleurs.nomCouleur)
        .filter(Niveau.id_ == niveau)
    )

    # Exécute la requête et récupère un seul résultat
    result = db.session.execute(stmt).first()

    # Vérifie si un niveau a été trouvé
    if result:
        niveau, hexCouleur = result

        return jsonify({
            "id": niveau.id_, 
            "nom": niveau.nom, 
            "description": niveau.description, 
            "duration": niveau.duration, 
            "difficulty": niveau.difficulty, 
            "color": hexCouleur,  # Remplace le nom par le code hex de la couleur
            "nbEvent": niveau.nbEvent
        }), 200

    else:       
        return jsonify({"error": "Aucun niveau trouvé"}), 404