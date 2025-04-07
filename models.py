from app import db


class Niveau(db.Model):
    __tablename__ = 'niveau'
    id_ = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    duree = db.Column(db.Integer, nullable=False)
    difficulte = db.Column(db.String(30), nullable=False)
    couleur = db.Column(db.String(6), nullable=False)
    minTemps = db.Column(db.Integer, nullable=False)
    maxTemps = db.Column(db.Integer, nullable=False)

class Evenement(db.Model):
    __tablename__ = 'evenement'
    id_ = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(30), nullable=False)
    description = db.Column(db.Text, nullable=False)
    duree = db.Column(db.Integer, nullable=False)
    couleur = db.Column(db.String(255), nullable=False)
    typeModule = db.Column(db.String(255), nullable=False)

class InstructionsDescriptions(db.Model):
    __tablename__ = 'InstructionDescriptions'
    nomModule = db.Column(db.String(128), primary_key=True)
    description = db.Column(db.Text, nullable=False)
    nomInstruction = db.Column(db.String(128), nullable=False)


class TraductionMatricule(db.Model):
    __tablename__ = 'TraductionMatricule'
    idMatricule = db.Column(db.String(6), primary_key=True, nullable=False)
    nomModule = db.Column(db.String(255), nullable=False)


class TraductionCouleurs(db.Model):
    __tablename__ = 'TraductionCouleurs'
    nomCouleur = db.Column(db.String(255), primary_key=True, nullable=False)
    hexCouleur = db.Column(db.String(6), nullable=False)


class WiresInstructions1(db.Model):
    __tablename__ = 'WiresInstructions1'
    id_ = db.Column(db.Integer, primary_key=True, nullable=False)
    fils4 = db.Column(db.String(1024), nullable=False)
    fils5 = db.Column(db.String(1024), nullable=False)
    fils6 = db.Column(db.String(1024), nullable=False)

    
class PatPlayInstructions1(db.Model):
    __tablename__ = 'PatPlayInstructions1'
    id_ = db.Column(db.Integer, primary_key=True, nullable=False)
    couleur = db.Column(db.String(255), nullable=False)
    carre = db.Column(db.Integer, nullable=False)
    cercle = db.Column(db.Integer, nullable=False)
    triangle = db.Column(db.Integer, nullable=False)
    x = db.Column(db.Integer, nullable=False)


class PatPlayInstructions2(db.Model):
    __tablename__ = 'PatPlayInstructions2'
    id_ = db.Column(db.Integer, primary_key=True, nullable=False)
    nbFinal = db.Column(db.Integer, nullable=False)
    ordre = db.Column(db.String(255), nullable=False)


class LightsInstructions1(db.Model):
    __tablename__ = 'LightsInstructions1'
    id_ = db.Column(db.Integer, primary_key=True, nullable=False)
    lumiere = db.Column(db.String(9), nullable=False)
    leviers = db.Column(db.String(6), nullable=False)


class BipolarityInstructions1(db.Model):
    __tablename__ = 'BipolarityInstructions1'
    id_ = db.Column(db.Integer, primary_key=True, nullable=False)
    lettre = db.Column(db.String(1), nullable=False)
    majuscule = db.Column(db.String(8), nullable=False)
    minuscule = db.Column(db.String(8), nullable=False)

class Utilisateur(db.Model):
    __tablename__ = 'Utilisateur'
    id_         = db.Column(db.Integer, primary_key=True, nullable=False)
    pseudo      = db.Column(db.String(255), nullable=False)
    mdp   	    = db.Column(db.String(255), nullable=False)
    admin       = db.Column(db.Integer, nullable=False, default=0)
    
	

