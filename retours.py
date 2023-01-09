#Fonction des codes retour pour les autres fonctions (code défi dans la RFC certains ajout et certains manque nécessaire fait après implémentation)
def analyseCodesRetours (code : int) :
    match (code) :
        case 1 : 
            print("Exportation annuaire : Erreur - impossible ouvrir le fichier annuaire")
        case 2 : 
            print("Importation annuaire : Erreur - impossible ouvrir le fichier annuaire")
        case 3 : 
            print("Ouverture de fichier impossible")
        case 4 : 
            print("ID contact non trouvé dans l'annuaire")
        case 10 : 
            print("Authentification : Succès")
        case 11 : 
            print("Authentification : Mot de passe incorrect")
        case 12 : 
            print("Authentification : Utilisateur inconnu")
        case 20 : 
            print("Récupération annuaire : Succès")
        case 21 : 
            print("Récupération annuaire  : Echec - droits insuffisants")
        case 22 :
            print("Récupération annuaire  : Echec - utilisteur inconnu")
        case 30 : 
            print("Création contact : Succès")
        case 31 : 
            print("Création contact : Echec - ID déja existant")
        case 32 : 
            print("Création contact : Echec - annuaire non trouvé pour l'ajout du contact")
        case 40 : 
            print("Modifier contact : Succès")
        case 41 : 
            print("Modifier contact : Echec - contact non trouvé")
        case 42 : 
            print("Modifier contact : Echec - coordonnées obligatoire saisie invalide")
        case 43 : 
            print("Création contact : Echec - annuaire non trouvé pour modification du contact")
        case 44 : 
            print("Création contact : Echec - ID contact non trouvé")
        case 50 : 
            print("Supprimer contact : Succès")
        case 51 : 
            print("Supprimer contact : Echec - contact non trouvé")
        case 52 : 
            print("Création contact : Echec - annuaire non trouvé pour suppression du contact")
        case 60 : 
            print("Ajouter droit utilisateur : Succès")
        case 61 : 
            print("Ajouter droit utilisateur : Echec - Utilisateur non trouvé")
        case 62 : 
            print("Ajouter droit utilisateur : Echec - ouverture du fichier pour l'ajout des droits impossible")
        case 63 : 
            print("Ajouter droit utilisateur : Echec - Utilisateur a déjà les droits")
        case 65 : 
            print("Supprimer droit utilisateur : Succès")
        case 66 : 
            print("Supprimer droit utilisateur : Echec - ouverture du fichier pour suppression des droits impossible")
        case 67 : 
            print("Supprimer droit utilisateur : Echec - l'utilisateur n'a pas les droits")
        case 70 : 
            print("Modifier mot de passe : Succès")
        case 71 : 
            print("Modifier mot de passe : Echec - Mot de passe trop grand")
        case 72 : 
            print("Modifier mot de passe : Echec - Caractère invalide")
        case 73 : 
            print("Modifier mot de passe : Echec - Mot de passe vide")
        case 80 :
            print("Créer utilisateur : Succès")
        case 81 :
            print("Créer utilisateur : Echec - utilisateur déjà existant")
        case 82 :
            print("Créer utilisateur : Echec - nombre d'utilisateur maximal existant déjà atteint")
        case 84 :
            print("Créer utilisateur : Echec - nom d'utilisateur vide")
        case 85 :
            print("Créer utilisateur : Echec - mot de passe vide")
        case 86:
            print("Créer utilisateur : Echec - erreur lors de l'encodement du message")
#Modifier utilisateur n'existe pas
#        case 90 :
#            print("Modifier utilisateur : Succès")
#        case 91 :
#            print("Modifier utilisateur : Echec")
#        case 92 :
#            print("Modifier utilisateur : Nom d'utilisateur invalide")
#Par contre changer mot de passe existe
        case 90 :
            print("Changer Mot de Passe : Succès")
        case 91 :
            print("Changer Mot de Passe : Echec - utilisateur non trouvé")
        case 92 :
            print("Changer Mot de Passe : Echec - ancien mot de passe invalide")
        case 93 :
            print("Changer Mot de Passe : Echec - mot de passe non valide")
        case 100 :
            print("Supprimer utilisateur : Succès")
        case 101 :
            print("Supprimer utilisateur : Echec - utilisateur non trouvé")
        case 102 :
            print("Supprimer utilisateur : Echec - nom d'utilisateur invalide")
        case 103 :
            print("Supprimer utilisateur : Droits insuffisant (non administrateur)")
        case 110 :
            print("Changement d'utilisateur : Succès")
        case 111 :
            print("Changement d'utilisateur : Echec - mot de passe invalide")
        case 112 :
            print("Changement d'utilisateur : Echec - utilisateur non trouvé")
        case _: #cas de code retour non présent ci dessus (ne devrait pas arriver mais sécurité)
            print("Erreur inconnu")

