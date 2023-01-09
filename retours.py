#Fonction des codes retour pour les autres fonctions (code défi dans la RFC certains ajout et certains manque nécessaire fait après implémentation)
def analyseCodesRetours (code : int) :
    match (code) :
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
        case 40 : 
            print("Modifier contact : Succès")
        case 41 : 
            print("Modifier contact : Echec - contact non trouvé")
        case 42 : 
            print("Modifier contact : Echec - coordonnées obligatoire saisie invalide")
        case 50 : 
            print("Supprimer contact : Succès")
        case 51 : 
            print("Supprimer contact : Echec - contact non trouvé")
        case 60 : 
            print("Ajouter droit utilisateur : Succès")
        case 61 : 
            print("Ajouter droit utilisateur : Echec - Utilisateur non trouvé")
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

