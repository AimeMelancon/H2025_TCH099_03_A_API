import bcrypt

from flask import jsonify
from app import db
from models import Admin


def creerAdmin(pseudo,mdp):
    """Cette méthode permet de communiquer à la base de donnée
        pour la création d'un administrateur.
        
    Paramètres:
        pseudo (String): Le pseudonyme de l'administrateur 
        mdp (String): Le mot de passe de l'administrateur
    """
    if not pseudo or not mdp:
        return jsonify({"error": "Les informations sont incomplètes veuillez réessayer."}), 400
    
    #Encodage selon la norme utf-8 du mot de passe et du pseudo de l'administrateur
    bytemdp = mdp.encode('utf-8')
    
    
    #Génération d'un "sel" sécurisé
    sel = bcrypt.gensalt()
    
    #Le mot de passe hashé
    hashpw = bcrypt.hashpw(bytemdp,sel)
   
    
    
    #Création d'un utilisateur admin
    new_Admin = Admin(pseudo=pseudo,mdp=hashpw)
    db.session.add(new_Admin)
    
    try:
        
        #Si le commit fonctionne envoie la réponse de succès. Sinon lance l'erreur.
        
        db.session.commit()
        return jsonify({"message": "La création de l'administrateur a bien été effectuée."}), 200
    
    except Exception as e:
        
        #Fait un rollback dans la base de donnée puis envoie l'erreur avec ses détails.
         
        db.session.rollback()  
        return jsonify({"error": f"Il y a un problème dans la création de l'administrateur : {str(e)}"}), 500
    
    
    