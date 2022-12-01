import UserUtils
import os


#La fonction creerUser va creer un nouveau utilisateur qui va lui meme créer un annuaire de part sa creation
def creerUser(userList : list, nom : str, password : str): 
	UserUtils.addUser(nom, password, userList)
    
	user = UserUtils.findUser(nom, userList)

	creerFichierAnuaire(user, "./users")


#La fonction doit pouvoir créer un fichier annuire. Ce dernier ne doit pas déjà exister 
#La création de l'annuaire se faire grace au nom de l'utilisateur qui est créer
def creerFichierAnuaire(user : UserUtils.User, pathFich : str): 

	NomUtilisteur = user.name

	if (os.path.exists(pathFich + "/" + NomUtilisteur + ".txt")) : 
		return -1 #Utilisateur existe déjà
	else :
	    #on prend le nomde l'utilisateur x : Yon.txt sera l'annuaire de l'utilisateur 'Yon' et on crée le fichier
		fichierAnnuaire = open(pathFich + "/" + NomUtilisteur + ".txt", 'w+')
		fichierAnnuaire.close()
		return 1 #L'annuaire a bien été créer
	    

#La fonction modifAnnuaire doit pouvoir modifier un annaire. Elle doit pouvoir : 
#Créer/modifier/supprimer un contact
#Ajouter/modifier des droits
def modifAnnuaire(userList : list, nom : str ,password : str, pathFich : str) : 

	user = UserUtils.findUser(nom, userList)
	NomUtilisteur = user.name
	passwd = UserUtils.checkPasswordUser(password,user)

	if(passwd == True ) : 
		if (not(os.path.exists(pathFich + "/" + NomUtilisteur + ".txt"))) : 
			return -1 #L'annuaire n'existe pas on ne peut donc pas le modifier
		else : 
			fichierAnnuaire = open(pathFich + "/" + NomUtilisteur + ".txt", 'a')
			fichierAnnuaire.write("test")
			fichierAnnuaire.close()
			return 1 #L'annuaire existe et a été modifier


    