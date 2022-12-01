import UserUtils
import os 

from pathlib import Path 


def creerUser(userList : list , password : str , nom : str): 

	UserUtils.addUser(nom,password,userList)

	user = UserUtils.findUser(nom,userList)

	creerFichierAnuaire(user , ".")

#La fonction doit pouvoir créer un fichier annuire. Ce dernier ne doit pas déjà exister 
#La création de l'annuaire se faire grace au nom de l'utilisateur qui est créer
def creerFichierAnuaire(user : UserUtils , pathFich : str): 


	NomUtilisteur = user.name

	pathFichier = Path(user.name).absolute()	#"Calcul" du chemin d'accès au fichier


	if (os.path.exists(pathFich + "/" + NomUtilisteur + ".txt")) : 
		return 81 #Utilisateur existe déjà
	else :
	#on prend le nomde l'utilisateur x : Yon.txt sera l'annuaire de l'utilisateur 'Yon' et on crée le fichier
		fichierAnnuaire = open(pathFichier + NomUtilisteur + ".txt", "w+")
	


#La fonction modifAnnuaire doit pouvoir modifier un annaire. Elle doit pouvoir : 
#Créer/modifier/supprimer un contact
#Ajouter/modifier des droits
###def modifAnnuaire(): 

###	print("Voulez-vous agir sur un contact ou ajouter/modifier des droits ?")
