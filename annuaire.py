import os


class Annuaire :
	owner = None
	userRights = None
	contacts = None
	def __init__(self, owner : str, userRights, contacts):
		self.owner = owner
		self.contacts = contacts[:]
		self.userRights = userRights[:]

def creerAnnuaire(username : str) :
	if (os.path.exists("./annuaires/" + username + ".txt")) : 
		os.remove("./annuaires/" + username + ".txt")
	#on prend le nomde l'utilisateur x : Yon.txt sera l'annuaire de l'utilisateur 'Yon' et on crée le fichier
	fichierAnnuaire = open("./annuaires/" + username + ".txt", 'w+')
	fichierAnnuaire.write(username)
	fichierAnnuaire.close()
	return None

def supprimerAnnuaire(username : str) :
	if (os.path.exists("./annuaires/" + username + ".txt")) : 
		os.remove("./annuaires/" + username + ".txt")

def importAnnuaire(username : str) :
	try :
		file = open("./annuaires/" + username + ".txt", 'r')
	except OSError:
		print("impossible d'ouvrir le fichier")
		return 2
	
	content = file.read()
	content = content.split('\n')

	rights = content[0].split(',')
	contacts = content[1:]

	for i in range(0, len(contacts)) :
		contacts[i] = contacts[i].split(',')
	
	ann = Annuaire(username, rights[:], contacts)
	return ann

def exportAnnuaire(ann : Annuaire) :
	try :
		file = open("./annuaires/" + ann.owner + ".txt", 'w')
	except OSError:
		print("impossible d'ouvrir le fichier")
		return 1

	file.write(','.join(ann.userRights))
	
	for contact in ann.contacts :
		file.write("\n" + ','.join(contact))
	
	file.close()

#peut etre refaite avec importAnnuaire(), ce qui la rendrais plus lisible
#60 succes
#62 err ouverture fich
#63 user a deja les droits
def addRightsAnnuaires(nomAnnuaire : str, username : str) :
	try :
		file = open("./annuaires/" + nomAnnuaire + ".txt", 'r')
	except OSError:
		print("impossible d'ouvrir le fichier")
		return 62
	
	content = file.read().split('\n')
	rights = content[0].split(',')
	file.close()

	if username in rights :
		return 63
	
	rights.append(username)
	file = open("./annuaires/" + nomAnnuaire + ".txt", 'w')

	file.write(rights[0])
	for user in rights[1:] :
		file.write("," + user)
	
	for c in content[1:] :
		file.write("\n" + c)
	file.close()
	return 60

#peut etre refaite avec importAnnuaire(), ce qui la rendrais plus lisible
#65 succes
#66 err ouverture fich
#67 user n a pas les droits
def removeRightsAnnuaires(nomAnnuaire : str, username : str) :
	try :
		file = open("./annuaires/" + nomAnnuaire + ".txt", 'r')
	except OSError:
		print("impossible d'ouvrir le fichier")
		return 66
	
	content = file.read().split('\n')
	rights = content[0].split(',')
	file.close()

	if username not in rights :
		return 67
	
	rights.remove(username)
	file = open("./annuaires/" + nomAnnuaire + ".txt", 'w')

	file.write(rights[0])
	for user in rights[1:] :
		file.write("," + user)
	
	for c in content[1:] :
		file.write("\n" + c)
	file.close()
	return 65
	
#ici username donne le nom de l'annuaire  dans lequel on ajoute le contacte
#30 succes
#32 annauire non trouver
def addContact(username : str, nom : str, prenom : str, mail : str, adresse : str = None, portable : str = None) :
	if adresse == None :
		adresse = ""
	if portable == None :
		portable = ""

	ann = importAnnuaire(username)
	if not isinstance(ann, Annuaire) :
		return 32

	if ann.contacts == [] :
		ID = str(1)
	else :	
		ID = str(int(ann.contacts[-1][0]) + 1 )
	
	ann.contacts.append([ID, nom, prenom, mail, adresse, portable])
	exportAnnuaire(ann)
	return 30


#40 succes
#42 ID non trouvé
#43 annuaire non trouvé	
def modifierContact(username : str, ID : int,  nom : str, prenom : str, mail : str, adresse : str = None, portable : str = None) :
	ann = importAnnuaire(username)
	if not isinstance(ann, Annuaire) :
		return 43

	IDhasbeenfound = False
	for i in range(0, len(ann.contacts)) :
		if ann.contacts[i][0] == str(ID) :
			ann.contacts[i] = [str(ID), nom, prenom, mail, adresse, portable]
			IDhasbeenfound = True

	if not IDhasbeenfound :
		return 42

	exportAnnuaire(ann)
	return 40

def rearrangeIDs(username : str) :
	ann = importAnnuaire(username)
	if not isinstance(ann, Annuaire) :
		return 4

	for i in range(1, len(ann.contacts)) :
		ann.contacts[i][0] = str(i+1)
	
	exportAnnuaire(ann)

def afficherAnnuaire(username : str) :
	ann = importAnnuaire(username)

	print("Qui a les droits : ")
	for right in ann.userRights :
		print("-", right)

	print("la liste de contacte :")
	for c in ann.contacts :
		print(f"{c[0]:4}| {c[1]:10}| {c[2]:10}| {c[3]:15}| {c[4]:20}| {c[5]:10}")

#ici username donne le nom de l'annuaire  dans lequel on supprime le contacte
#ID est l'ID du contacte à supprimer
#50 succes
#51 contact non trouvé
#52 annuaire non trouvé
def removeContact(username : str, ID : int) :
	ann = importAnnuaire(username)
	if not isinstance(ann, Annuaire) :
		return 52

	IDtrouve = False
	for c in ann.contacts :
		if c[0] == str(ID) :
			ann.contacts.remove(c)
			IDtrouve = True
	exportAnnuaire(ann)
	rearrangeIDs(username)

	if (IDtrouve) :
		return 50
	else :
		return 51
