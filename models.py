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

class Fils(db.Model):
    __tablename__ = 'Fils'
    id_ = db.Column(db.Integer, primary_key=True, nullable=False)
    nbFils = db.Column(db.Integer, nullable=False)
    couleurFil1 = db.Column(db.String(255), nullable=True)
    couleurFil2 = db.Column(db.String(255), nullable=True)
    couleurFil3 = db.Column(db.String(255), nullable=True)
    couleurFil4 = db.Column(db.String(255), nullable=True)
    couleurFil5 = db.Column(db.String(255), nullable=True)
    couleurFil6 = db.Column(db.String(255), nullable=True)
    solution = db.Column(db.Integer, nullable=False)


class FilsInstructions1(db.Model):
    __tablename__ = 'FilsInstructions1'
    id_ = db.Column(db.Integer, primary_key=True, nullable=False)
    fils4 = db.Column(db.String(1024), nullable=False)
    fils5 = db.Column(db.String(1024), nullable=False)
    fils6 = db.Column(db.String(1024), nullable=False)
    

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
    

class Lights(db.Model):
    __tablename__ = 'Lights'
    id_ = db.Column(db.Integer, primary_key=True, nullable=False)
    lumiere = db.Column(db.String(9), nullable=False)
    solution = db.Column(db.String(6), nullable=False)


class LightsInstructions1(db.Model):
    __tablename__ = 'LightsInstructions1'
    id_ = db.Column(db.Integer, primary_key=True, nullable=False)
    lumiere = db.Column(db.String(9), nullable=False)
    leviers = db.Column(db.String(6), nullable=False)
    

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


class BipolariteInstructions1(db.Model):
    __tablename__ = 'BipolariteInstructions1'
    id_ = db.Column(db.Integer, primary_key=True, nullable=False)
    lettre = db.Column(db.String(1), nullable=False)
    majuscule = db.Column(db.String(8), nullable=False)
    minuscule = db.Column(db.String(8), nullable=False)

class Admin(db.Model):
    __tablename__ = 'Admin'
    id_         = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    pseudo      = db.Column(db.String(255), unique=True, nullable=False)
    mdp   	    = db.Column(db.String(255), nullable=False)
    gererModule = db.Column(db.Integer, nullable=True)
    gererEvent  = db.Column(db.Integer, nullable=True)
    gererDebug  = db.Column(db.Integer, nullable=True)
	
	