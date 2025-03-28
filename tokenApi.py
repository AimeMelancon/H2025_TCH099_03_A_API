import jwt
from flask import  current_app,request,jsonify


#'Permet de  vérifier si le token est valide ou non.'

def token_required(f):
    def decorated(*args,**kwargs):
        #Permet de récupérer le token dans le json
        data = request.get_json()
        #Si les données existe, il récupère le token
        token = data.get('token') if data else None
        
        #S'il manque un token, il renvoie une erreur
        if not token:
            return jsonify({"error":"La requête manque un token"}),403
        
        try:
            #En encore le token qui est en String en bytes    
            token_bytes = token.encode('utf-8')

            #En décode le token et si oui on laisse cours à la transaction courante.
            jwt.decode(token_bytes,current_app.config['secret_key'],algorithms="HS256")
        except Exception as e:
            #Si le token est invalide ou expiré lance une exception avec une erreur 400.
            return jsonify({"error":f"Le token est expiré ou invalide "}),400
        return f(*args,**kwargs)
    return decorated