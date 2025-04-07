from flask import jsonify
from sqlalchemy import Select
from app import db
from models import Utilisateur
from flask_bcrypt import generate_password_hash

def creerUtilisateur(pseudo, mdp):
    """Cette méthode permet de communiquer à la base de donnée
       pour la création d'un utilisateur.

    Paramètres:
        pseudo (String): Le pseudonyme de l'utilisateur 
        mdp (String): Le mot de passe de l'utilisateur
    """
    if not pseudo or not mdp:
        return jsonify({"error": "Les informations sont incomplètes veuillez réessayer."}), 400

    try:

       #Vérifie que l'utilisateur n'existe pas 
        stmt = (Select(Utilisateur)
                .filter(Utilisateur.pseudo == pseudo)
                )
        
        
        result = db.session.execute(stmt).scalars().first()
        
        if not result:
            
            #hash le mot de passe avant de le mettre dans la db
            hashmdp = generate_password_hash(mdp)
            
            # Création de l'utilisateur admin
            new_admin = Utilisateur(pseudo=pseudo, mdp=hashmdp, admin=0)
            db.session.add(new_admin)
            db.session.commit()
        
            return jsonify({"message": "La création de l'utilisateur a bien été effectuée."}), 200
        
        else:
            return jsonify({"error": f"Il y a un problème dans la création de l'utilisateur."}), 500

    except Exception as e:
            db.session.rollback()
            return jsonify({"error": f"Il y a un problème dans la création de l'utilisateur."}), 500