from flask import current_app, jsonify
from app import db
from models import Utilisateur
import datetime
from sqlalchemy import Select
from flask_bcrypt import check_password_hash
import jwt
import sys

def coUser(pseudo,mdp):
    """Permet de se connecter dans un compte user.

    Paramètres:
        pseudo (String): Le pseudo
        mdp (String): Le mot de passe
    """
    
    try:
         stmt = (
            Select(Utilisateur)
            .filter(Utilisateur.pseudo == pseudo)
         )
         
         result =db.session.execute(stmt).scalars().first()
         #Permet de vérifier si l'identifiant est valide
         if result:
             
             # Encodage du mot de passe de l'utilisateur
            connect = check_password_hash(result.mdp,mdp)
             #Permet de vérifier la connexion avec le mot de passe
            if connect:
                 #Génère un token
                 token = jwt.encode({'pseudo': pseudo, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=12)},current_app.config['secret_key'],algorithm="HS256")
                 
                 #Prépare la réponse en boolean pour savoir si c'est un admin ou nom
                 estAdmin=True if result.admin == 1 else False
                 #Renvoie la réponse à la requête positive
                 return jsonify({"connexion" : True, "utilisateur": pseudo ,"admin" : estAdmin , "token": token}),200
            else:
                 return jsonify({"error":"L'identifiant ou le mot de passe fournie n'est pas valide."}),401
         else:
             return jsonify({"error":"L'identifiant ou le mot de passe fournie n'est pas valide."}),401
    except Exception as e:
        return jsonify({"error":f"Échec de la connexion veuillez réessayer: {e}"}),404