
#Un contact  a 4 champs obligatoire : ID , nom, prenom, adresse mail
class Contact :
    def __init__(self, ID : int = "1" , nom : str = "Yon", prenom :  str = "None", email : str = "None", telephone : str = None, adressePostal : str = None):
        self.ID = ID
        self.nom = nom
        self.prenom = prenom
        self.email = email 

#Mettre plus tard si necessaire les fonction de utils dedans. Problème avec les classes