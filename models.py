from app import db

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Niveau(db.Model):
    __tablename__ = 'niveau'
    id_ = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    difficulty = db.Column(db.String(30), nullable=False)
    color = db.Column(db.String(6), nullable=False)
    nbEvent = db.Column(db.Integer, nullable=False)

class Evenement(db.Model):
    id_ = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(30), nullable=False)
    description = db.Column(db.Text, nullable=False)
    duree = db.Column(db.Integer, nullable=False)
    difficulte = db.Column(db.String(30), nullable=False)
    couleur = db.Column(db.String(255), nullable=False)
    typeModule = db.Column(db.Integer, nullable=False)


class TraductionMatricule(db.Model):
    __tablename__ = 'TraductionMatricule'
    idMatricule = db.Column(db.Integer, primary_key=True, nullable=False)
    nomModule = db.Column(db.String(255), nullable=False)

class TraductionInstructions(db.Model):
    __tablename__ = 'TraductionInstructions'
    idModule = db.Column(db.Integer, primary_key=True, nullable=False)
    nomInstructions = db.Column(db.String(255), nullable=False)

class TraductionCouleurs(db.Model):
    __tablename__ = 'TraductionCouleurs'
    nomCouleur = db.Column(db.String(255), primary_key=True, nullable=False)
    hexCouleur = db.Column(db.String(6), nullable=False)

class Fils(db.Model):
    __tablename__ = 'Fils'
    id_ = db.Column(db.Integer, primary_key=True, nullable=False)
    nbFils = db.Column(db.Integer, nullable=False)
    couleurFil1 = db.Column(db.String(255), nullable=False)
    couleurFil2 = db.Column(db.String(255), nullable=False)
    couleurFil3 = db.Column(db.String(255), nullable=False)
    couleurFil4 = db.Column(db.String(255), nullable=False)
    couleurFil5 = db.Column(db.String(255), nullable=False)
    couleurFil6 = db.Column(db.String(255), nullable=False)
    solution = db.Column(db.Integer, nullable=False)

class FilsInstructions(db.Model):
    __tablename__ = 'FilsInstructions'
    id_ = db.Column(db.Integer, primary_key=True, nullable=False) 
    description = db.Column(db.String(1024), nullable=False)
    FilsInstruction1id = db.Column(db.Integer, db.ForeignKey('FilsInstruction1.id_'), nullable=False)
    
    fils_instruction1 = db.relationship('FilsInstruction1', back_populates='instructions')

class FilsInstruction1(db.Model):
    __tablename__ = 'FilsInstruction1'
    id_ = db.Column(db.Integer, primary_key=True, nullable=False)
    fils4 = db.Column(db.String(1024), nullable=False)
    fils5 = db.Column(db.String(1024), nullable=False)
    fils6 = db.Column(db.String(1024), nullable=False)
    
    instructions = db.relationship('FilsInstructions', back_populates='fils_instruction1')

class PatPlay(db.Model):
    __tablename__ = 'PatPlay'
    id_ = db.Column(db.Integer, primary_key=True, nullable=False)
    couleurTriangle = db.Column(db.String(255), nullable=False)
    couleurCercle = db.Column(db.String(255), nullable=False)
    couleurCarre = db.Column(db.String(255), nullable=False)
    couleurX = db.Column(db.String(255), nullable=False)
    formeHG = db.Column(db.String(255), nullable=False)
    formeHD = db.Column(db.String(255), nullable=False)
    formeBG = db.Column(db.String(255), nullable=False)
    formeBD = db.Column(db.String(255), nullable=False)
    solution = db.Column(db.String(255), nullable=False)

class PatPlayInstructions(db.Model):
    __tablename__ = 'PatPlayInstructions'
    id_ = db.Column(db.Integer, primary_key=True, nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    PatPlayInstructions1id = db.Column(db.Integer, db.ForeignKey('PatPlayInstructions1.id_'), nullable=False)
    PatPlayInstructions2id = db.Column(db.Integer, db.ForeignKey('PatPlayInstructions2.id_'), nullable=False)
    
    instruction1 = db.relationship('PatPlayInstructions1', back_populates='instructions')
    instruction2 = db.relationship('PatPlayInstructions2', back_populates='instructions')

class PatPlayInstructions1(db.Model):
    __tablename__ = 'PatPlayInstructions1'
    id_ = db.Column(db.Integer, primary_key=True, nullable=False)
    couleur = db.Column(db.String(255), nullable=False)
    carre = db.Column(db.Integer, nullable=False)
    cercle = db.Column(db.Integer, nullable=False)
    triangle = db.Column(db.Integer, nullable=False)
    x = db.Column(db.Integer, nullable=False)
    
    instructions = db.relationship('PatPlayInstructions', back_populates='instruction1')

class PatPlayInstructions2(db.Model):
    __tablename__ = 'PatPlayInstructions2'
    id_ = db.Column(db.Integer, primary_key=True, nullable=False)
    nbFinal = db.Column(db.Integer, nullable=False)
    ordre = db.Column(db.String(255), nullable=False)
    
    instructions = db.relationship('PatPlayInstructions', back_populates='instruction2')

class Lights(db.Model):
    __tablename__ = 'Lights'
    id_ = db.Column(db.Integer, primary_key=True, nullable=False)
    lumiere = db.Column(db.String(9), nullable=False)
    solution = db.Column(db.String(6), nullable=False)

class LightsInstructions(db.Model):
    __tablename__ = 'LightsInstructions'
    id_ = db.Column(db.Integer, primary_key=True, nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    LightsInstructions1id = db.Column(db.Integer, db.ForeignKey('LightsInstructions1.id_'), nullable=False)
    
    instruction1 = db.relationship('LightsInstructions1', back_populates='instructions')

class LightsInstructions1(db.Model):
    __tablename__ = 'LightsInstructions1'
    id_ = db.Column(db.Integer, primary_key=True, nullable=False)
    lumiere = db.Column(db.String(9), nullable=False)
    leviers = db.Column(db.String(6), nullable=False)
    
    instructions = db.relationship('LightsInstructions', back_populates='instruction1')

class Bipolarite(db.Model):
    __tablename__ = 'Bipolarite'
    id_ = db.Column(db.Integer, primary_key=True, nullable=False)
    lettre1 = db.Column(db.String(1), nullable=False)
    lettre2 = db.Column(db.String(1), nullable=False)
    lettre3 = db.Column(db.String(1), nullable=False)
    lettre4 = db.Column(db.String(1), nullable=False)
    caseChoisie = db.Column(db.Integer, nullable=False)
    couleur = db.Column(db.String(255), nullable=False)
    solution = db.Column(db.String(255), nullable=False)

class BipolariteInstructions(db.Model):
    __tablename__ = 'BipolariteInstructions'
    id_ = db.Column(db.Integer, primary_key=True, nullable=False)
    description = db.Column(db.String(1024), nullable=False)
    BipolariteInstructions1id = db.Column(db.Integer, db.ForeignKey('BipolariteInstructions1.id_'), nullable=False)
    
    instruction1 = db.relationship('BipolariteInstructions1', back_populates='instructions')

class BipolariteInstructions1(db.Model):
    __tablename__ = 'BipolariteInstructions1'
    id_ = db.Column(db.Integer, primary_key=True, nullable=False)
    lettre = db.Column(db.String(1), nullable=False)
    majuscule = db.Column(db.String(8), nullable=False)
    minuscule = db.Column(db.String(8), nullable=False)
    
    instructions = db.relationship('BipolariteInstructions', back_populates='instruction1')
