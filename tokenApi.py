import jwt
from flask import  app,request,jsonify


#'Permet de  vérifier si le token est valide ou non.'

def token_required(f):
    def decorated(*args,**kwargs):
        token = request.get_json('token')
        if not token:
            return jsonify({"error":"La requête manque un token"}),403
        try:
            jwt.decode(token,app.config['secret_key'],algorithms="HS256")
        except Exception as e:
            return jsonify({"error":"Le token est expiré ou invalide"})
        return f(*args,**kwargs)
    return decorated