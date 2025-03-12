from api.v1.instructions.getInstructions import getInstruction
from api.v1.modules.verifyMatricule import verifyMatricule
from api.v1.niveaux.getNiveaux import getNiveaux
from api.v1.modules.getModule import getModule
from flask import make_response

def initialize_routes(app):
    
    @app.route('/api/v1/instructions/<matricule>', methods=['GET'])
    def instruction(matricule):
        data = getInstruction(matricule)

        # Préparer une réponse
        response = make_response(data)
        
        # Set les headers de la réponse.
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        
        return response
    

    @app.route('/api/v1/<module>/<matricule>', methods=['GET'])
    def verify(module, matricule):

        boolean = verifyMatricule(module, matricule)

        # Préparer une réponse
        response = make_response(boolean)
        
        # Set les headers de la réponse.
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = 'application/json; charset=utf-8'

        return response
    
    @app.route('/api/v1/niveaux',methods=['GET'])
    def niveaux():
        
        # Récupérer la liste de niveaux
        data = getNiveaux()
        
        # Préparer la réponse
        response  = make_response(data)
        
         # Set les headers de la réponse.
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        
        return response
    
    @app.route('/api/v1/<module>', method=['GET'])
    def module(module):
        
        # Récupérer le module demandé
        data = getModule(module)
        
        #Préparation de la réponse
        response = make_response(data)
        
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = 'application/json; charset=utf-8'
        
        return response

    
