from flask import jsonify
from app import db
from models import Admin

def creerAdmin(pseudo, mdp):
    """Cette méthode permet de communiquer à la base de donnée
       pour la création d'un administrateur.

    Paramètres:
        pseudo (String): Le pseudonyme de l'administrateur 
        mdp (String): Le mot de passe de l'administrateur
    """
    if not pseudo or not mdp:
        return jsonify({"error": "Les informations sont incomplètes veuillez réessayer."}), 400

    try:
        # Hash du mot de passe avec Flask-Bcrypt

        # Création de l'utilisateur admin
        new_admin = Admin(pseudo=pseudo, mdp=mdp)
        db.session.add(new_admin)
        db.session.commit()

        return jsonify({"message": "La création de l'administrateur a bien été effectuée."}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Il y a un problème dans la création de l'administrateur : {str(e)}"}), 500
