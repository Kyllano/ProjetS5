import UserUtils
from os import *

def creerUser(): 
	

#La fonction doit pouvoir créer un fichier annuire. Ce dernier ne doit pas déjà exister 
#La création de l'annuaire se faire grace au nom de l'utilisateur qui est créer
def creerFichierAnuaire(): 

	pathFichier = path(NomUtilisteur).absolute()	#"Calcul" du chemin d'accès au fichier

	Utilisateur = UserUtils.User()
	NomUtilisteur = Utilisateur.getNameUser()

	if (os.path.exists(pathFichier + NomUtilisteur + ".txt")) : 
		return 81 #Utilisateur existe déjà
	else :
	#on prend le nomde l'utilisateur x : Yon.txt sera l'annuaire de l'utilisateur 'Yon' et on crée le fichier
		fichierAnnuaire = open(pathFichier + NomUtilisteur + ".txt", "w+")
	


#La fonction modifAnnuaire doit pouvoir modifier un annaire. Elle doit pouvoir : 
#Créer/modifier/supprimer un contact
#Ajouter/modifier des droits
###def modifAnnuaire(): 

###	print("Voulez-vous agir sur un contact ou ajouter/modifier des droits ?")
