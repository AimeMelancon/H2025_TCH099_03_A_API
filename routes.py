from api.v1.niveaux.getNiveaux import getNiveaux
from api.v1.instructions.getInstructions import getInstructions
from api.v1.utilisateurs.postAdmin import creerAdmin
from flask import make_response, request, jsonify
from app import db
from tokenApi import token_required
from sqlalchemy import Select
from api.v1.utilisateurs.getUser import coUser
from api.v1.utilisateurs.postUtilisateurs import creerUtilisateur
from algorithme.filsAlgo import filsAlgo
from algorithme.lightsAlgo import lightsAlgo
from algorithme.patplayAlgo import patplayAlgo
from algorithme.polariteAlgo import polariteAlgo
from models import Evenement, TraductionCouleurs, TraductionMatricule
import random



def initialize_routes(app):

    @app.route('/api/v1/niveaux',methods=['GET'])
    def niveaux():
        """Route qui récupère tous les niveaux présents dans la base de données."""

        # Récupérer la liste de niveaux
        data = getNiveaux()
        
        # Préparer la réponse
        response  = make_response(data)
        
         # Set les headers de la réponse.

        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        
        return response  

    @app.route('/api/v1/verify', methods=['GET'])
    def instructions():
        """Route qui récupères les instructions pour un module et matricule fourni
           '/api/v1/verify?matricule=<matricule>&module=<module>'
        """

        # Récupère les paramètres après le ?
        module = request.args.get("module")
        matricule = request.args.get("matricule")

        # Vérifier le module & matricule et retourner les instructions s'il y a lieu.
        data = getInstructions(module, matricule)
        
        # Préparer la réponse
        response  = make_response(data)
        
        # Set les headers de la réponse.
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        
        return response
    

    @app.route('/api/v1/admin', methods=['POST'])
    @token_required
    def inscriptionAdmin():
        """Route qui permet de créer un administrateur grâce à
            {  "pseudo" :"<pseudo>",
                "mdp"   : "<mdp>",
                "token" : "<token>"
            }"""
        
        data = request.get_json()

        if not data or 'pseudo' not in data or 'mdp' not in data:
            return jsonify({"error": "Les champs 'pseudo' et 'mdp' sont requis."}), 400

        #Récupération des données pour la création du compte
        pseudo = data['pseudo']
        mdp = data['mdp']
        
        #Création d'un compte admin    
        response = creerAdmin(pseudo,mdp)
        
        return response
    
    @app.route('/api/v1/login', methods=['POST'])
    def connexionAdmin():
        """Route qui permet de se connecter à un compte.
           Requête attendue : JSON avec 'pseudo' et 'mdp'

            Exemple :
            POST /api/v1/login
            {
                "pseudo": "admin1",
                "mdp": "motdepasse"
            }
            """
           
        data = request.get_json()

        if not data or 'pseudo' not in data or 'mdp' not in data:
            return jsonify({"error": "Les champs 'pseudo' et 'mdp' sont requis."}), 400

        pseudo = data['pseudo']
        mdp = data['mdp']
        
        data = coUser(pseudo,mdp)
        
        #Préparation de la réponse
        response = make_response(data)
        
         # Set les headers de la réponse.
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        
        return response
        
    
    @app.route('/api/v1/utilisateur', methods=['POST'])
    def inscriptionUser():
        """Route qui permet de créer un utilisateur grâce à
            {  "pseudo" :"<pseudo>",
                "mdp" : "<mdp>"                
            }"""
        
        data = request.get_json()

        if not data or 'pseudo' not in data or 'mdp' not in data:
            return jsonify({"error": "Les champs 'pseudo' et 'mdp' sont requis."}), 400

        #Récupération des données pour la création du compte
        pseudo = data['pseudo']
        mdp = data['mdp']
        
        #Création d'un compte admin    
        response = creerUtilisateur(pseudo,mdp)
        
        return response
    
    @app.route('/api/v1/module', methods=['GET'])
    def getModule():
        module = request.args.get("module")
        typeModule = ""

        if module.lower().capitalize() == "Wires":
            data = filsAlgo()
            typeModule = "Wires"

        elif module.lower().capitalize() == "Lights":
            data = lightsAlgo()
            typeModule = "Lights"

        elif module.lower().capitalize() == "Bipolarity":
            data = polariteAlgo()
            typeModule = "Bipolarity"

        elif module.lower().replace('p', 'P') == "PatPlay":
            data = patplayAlgo()
            typeModule = "PatPlay"

        else:
            return jsonify({'erreur': "Module non trouvé"}), 404 
        
        # Récupérer les informations sur l'événement
        stmt = (Select(Evenement, TraductionCouleurs.hexCouleur, TraductionMatricule.idMatricule)
                .join(TraductionCouleurs, TraductionCouleurs.nomCouleur == Evenement.couleur)
                .join(TraductionMatricule, TraductionMatricule.nomModule == Evenement.typeModule)
                .filter(Evenement.typeModule == typeModule)
                )
        results = db.session.execute(stmt).all()

        if results:

            results_list = [
                            {
                                "id_": row.id_,
                                "nom": row.nom,
                                "description": row.description,
                                "duree": row.duree,
                                "couleur": hexCouleur,
                                "typeModule": row.typeModule,
                                "matricule" : matricule
                            }
                            for row, hexCouleur, matricule in results
                    ]
        else:
            return jsonify({'erreur': "Événement non trouvé"}), 404 


        fetch_length = len(results)
        random_module_index = random.randint(0, fetch_length - 1)
        random_event_dic = results_list[random_module_index]

        response_content = {"module": data, "eventData": random_event_dic}

         # Préparer la réponse
        response  = make_response(jsonify(response_content))
        
        # Set les headers de la réponse.

        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = 'application/json; charset=utf-8'

        return response

        
    
    @app.route('/api/v1/testDeConnexion', methods=['POST'])  
    @token_required
    def testCo():
        """Route qui permet de vérifier un token
           {
                "token" : "<token>"
           }"""
        data = request.get_json()
       
        if not data or 'token' not in data:
            return jsonify({"error": "Il manque un token."}), 400
        
        response = jsonify({"test": True})
        
        return response
    
    @app.route("/api/v1",methods=['GET'])
    def apiCo():
        """Route qui permet de vérifier que l'api est bien connectée"""
        
        data = jsonify({"estConnecte":True})
        
        response = make_response(data)
        
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        
        return response
        

    
