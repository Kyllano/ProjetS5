import UserUtils
import annuaire


def ajouterUserCmd(username : str, password : str, userlist : list) :
    retour = UserUtils.addUser(username, password, userlist)
    match (retour) :
        case 0 :
            print("Utilisateur ajouté avec succès")
        case -1 :
            print("Nom d'utilisateur invalide")
        case -2 :
            print("Mot de passe invalide")
        case -3 :
            print("Cet utilisateur existe deja")

def removeUserCmd(username : str, userlist : list) :
    retour = UserUtils.removeUser(username, userlist)
    match (retour) :
        case 0 :
            print("Utilisateur supprimé avec succès")
        case -1 :
            print("Nom d'utilisateur invalide")
        case -3 :
            print("Utilisateur deja supprimé ou inexistant")
    annuaire.supprimerAnnuaire(username)
