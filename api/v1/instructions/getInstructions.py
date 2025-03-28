from flask import jsonify

from models import TraductionMatricule, InstructionsDescriptions, PatPlayInstructions1, PatPlayInstructions2
from sqlalchemy import Select
from app import db

def getInstructions(module, matricule):
    """Vérifie si le module et le matricules existent et sont liés; si oui, retourner leurs description et instructions.

    Route associée: '/api/v1/verify?matricule=<matricule>&module=<module>', méthodes: GET
    P.S: matricule= et module= sont interchangeables de place.

    Paramètres:
      matricule (str) (case-sensitive): Le matricule (exemple: ABC123, XYZ789)
      module (str) (case-sensitive): Le nom du module parmi les suivants: ["Lights", "Bipolarite", "PatPlay", "Fils"]

    Retour:
      Si le module et matricule existent et son liés:

        Si le module est PatPlay:
          Description et 2 liste de dictionnaires (hashmap) représentant chacune des lignes de chaque table d'instruction du PatPlay.  


          {"description": ... ,
          "instructions1": [{"carre", valeur},
                            {...} ],
          "instructions2": [{id: valeur},
                            {...}]                 
          }

        Si le module est autre que PatPlay:
          Description et liste de dictionnaires (hashmap) représentant chacune des lignes de la table d'instruction du module.    
        
          {"description": ... ,
          "instructions": [{"attribut", valeur},
                            {...} ],               
          }

        Réponse HTTP: 200 OK

      Sinon:
        {"result": false}
        Réponse HTTP: 404 Not Found
    """

    # Le nom du module n'est pas case-sensitive côté front-end
    # On doit donc le rendre conforme au nom de la table de la db.
    # Ex: PatPlay, Lights, Wires, Bipolarity
    if module.lower() == "patplay":
        module = module.lower().replace('p', 'P')
    else:
        module = module.lower().capitalize()

    # Le matricale n'est pas case-sensitive côté front-end
    # On doit donc le rendre conforme avec la DB (Uppercase)
    matricule = matricule.upper()    

    # Requête SQL
    stmt = (
        Select(TraductionMatricule)
        .filter(TraductionMatricule.idMatricule == matricule, TraductionMatricule.nomModule == module)
    )
    # Exécution de la requête
    result = db.session.execute(stmt).scalars().first()

    # Module et matricule inexistants ou non liés
    if result is None:
        return jsonify({"result": False}), 404

    #------ Module et matricule existent et son liés ------
    # Cas spécial: PatPlay (2 tables)

    if module =='PatPlay':

        # Requêtes SQL
        stmt_desc = (Select(InstructionsDescriptions.description)
                    .filter(InstructionsDescriptions.nomModule == 'PatPlay'))

        stmt_inst1 = Select(PatPlayInstructions1)
        stmt_inst2 = Select(PatPlayInstructions2)


        # Exécution des requêtes
        patplay_description = db.session.execute(stmt_desc).scalars().first()
        patplay_instructions1 = db.session.execute(stmt_inst1).scalars().all()
        patplay_instructions2 = db.session.execute(stmt_inst2).scalars().all()

        # Transforme en dictionnaire la première table d'instruction
        patplay_instructions1 = [
            {
                "id_": inst.id_,
                "couleur": inst.couleur,
                "carre": inst.carre,
                "cercle": inst.cercle,
                "triangle": inst.triangle,
                "x": inst.x
            }
            for inst in patplay_instructions1
        ]

        # Transforme en dictionnaire la deuxième table d'instruction
        patplay_instructions2 = [
            {
                "id_": inst.id_,
                "nbFinal": inst.nbFinal,
                "ordre": inst.ordre
            }
            for inst in patplay_instructions2
        ]

        return jsonify({
            'description': patplay_description,
            "instructions1": patplay_instructions1,
            "instructions2": patplay_instructions2
        }), 200
    
    # Fetch description & instructions des autres module que PatPlay
    else:
        # String de la table d'instructions à accéder
        tablename = f'{module}Instructions1'


        # Requêtes SQL
        stmt_desc = (Select(InstructionsDescriptions.description)
                    .filter(InstructionsDescriptions.nomModule == module))
        description = db.session.execute(stmt_desc).scalars().first()
        

        # Récupérer la table à accéder selon le module en argument
        table = db.Model.metadata.tables.get(tablename)

        # Récupère les instructions
        stmt_instructions = Select(table)

        # Type: liste de tuples avec chaque colonne [(id, lettre, maj, min) , (...)]
        results = db.session.execute(stmt_instructions).all()

        # Transformer chaque résultat de la requête en un dictionnaire, ou chaque nom de colonne est la clé, avec les valeurs des tuples en valeur de dict.
        # Type liste de dictionnaire [{"id_": 1,"lettre": "A","majuscule": "01000001","minuscule": "01100001"}, {...}]
        instructions = [dict(row._mapping) for row in results]

        return jsonify({"description": description, "instructions": instructions}), 200
        
        



            

        
