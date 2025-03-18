from flask import jsonify
from models import Evenement, TraductionCouleurs
from sqlalchemy import Select
from app import db

def getEvent(id_event):
    """Si l'id existe pour l'évènement il le retourne sinon il envoie une erreur.
    
        Route associée: /api/v1/events/<id_event>    

        Paramètre: 
        id_event (int): L'id de l'évènement en cours dans l'application
        
        
        Retour :
        
          Si l'id_event est correct:
            Retourne l'évènement en entier avec tous ses attributs
            Réponse HTTP: 200 OK


        
          Sinon:
            {"error":"Aucun évènement trouvé."}
            Réponse HTTP: 404 Not Found
    
    """
    
    #Requête SQLite
    stmt =(
        
        Select(Evenement,TraductionCouleurs.hexCouleur)
        .join(TraductionCouleurs, Evenement.couleur == TraductionCouleurs.nomCouleur)
        .filter(Evenement.id_ == id_event)
    
    )
    
    # Exécute la requête et récupère un seul résultat
    result = db.session.execute(stmt).first()
    
    
    #On vérifie si on a pu récupérer se qu'on a cherché dans la db
    if result :
        
        event, hexCouleur = result
        #On renvoie un json de la réponse de la requête positive
        return jsonify({
            "id_": event.id_,
            "nom":event.nom,
            "description":event.description,
            "duree":event.duree,
            "couleur": hexCouleur,
            "typeModule":event.typeModule
        }),200
    
    else:
        #On envoie un json de la réponse de la requête négative
        return jsonify({
            "error":"Aucun évènement trouvé."
        }),404
