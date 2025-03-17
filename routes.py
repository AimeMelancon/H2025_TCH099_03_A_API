from api.v1.niveaux.getNiveau import getNiveau
from api.v1.niveaux.getNiveaux import getNiveaux
from api.v1.instructions.getInstructions import getInstructions
from flask import make_response, request

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
    
    @app.route('/api/v1/niveaux/<int:niveau>',methods=['GET'])
    def niveau_indiv(niveau):
        """Route qui récupère le niveau spécifié de la base de données."""

        # Récupérer la liste de niveaux
        data = getNiveau(niveau)
        
        # Préparer la réponse
        response  = make_response(data)
        
         # Set les headers de la réponse.
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        
        return response
    
    @app.route('/api/v1/verify', methods=['GET'])
    def instructions():
        """Route qui récupères les instructions pour un module et matricule fourni"""
        module = request.args.get("module")
        matricule = request.args.get("matricule")

        # Récupérer la liste de niveaux
        data = getInstructions(module, matricule)
        
        # Préparer la réponse
        response  = make_response(data)
        
         # Set les headers de la réponse.
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        
        return response
    
