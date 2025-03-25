from flask import app, jsonify
from app import db
from models import Utilisateur
import datetime
from sqlalchemy import Select
import bcrypt
import jwt


def coAdmin(pseudo,mdp):
    """Permet de se connecter en temps qu'administrateur

    Paramètres:
        pseudo (String): Le pseudo de l'admin
        mdp (String): Le mot de passe de l'admin
    """
    
    try:
         stmt = (
            Select(Utilisateur)
            .filter(Utilisateur.pseudo == pseudo))
         
         result =db.session.execute(stmt).first()
         #Permet de vérifier si l'identifiant est valide
         if result:
             
             # Encodage du mot de passe de l'utilisateur
            userMDP = mdp.encode('utf-8') 
             
            connect = bcrypt.checkpw(userMDP,result.mdp)
             #Permet de vérifier la connexion avec le mot de passe
            if connect:
                 #Génère un token
                 token = jwt.encode({'pseudo': pseudo, "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=15)},app.config['secret_key'])
                 #Renvoie la réponse à la requête positive
                 return jsonify({"Connexion" : True, "Utilisateur": pseudo , "token": token }),200
            else:
                 return jsonify({"error":"L'identifiant ou le mot de passe fournie n'est pas valide."}),401
         else:
             return jsonify({"error":"L'identifiant ou le mot de passe fournie n'est pas valide."}),401
    except Exception as e:
        return jsonify({"error":"Échec de la connexion veuillez réessayer"}),404