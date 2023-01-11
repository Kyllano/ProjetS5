from cryptography.hazmat.primitives import hashes
import random
import string
import annuaire
import os


class User :
    #Avec un nom et un mot de passe donné, créer un utilisateur ayant un nom et un mot de passe.
    #Le mot de passe sera digéré en sha256 et 
    def __init__(self, name : str, password : str, alreadyExists : bool, passwordSalt : str = None):
        self.name = name

        #Si l'user existe déja, on ne fait qu'ajouter les champs suivants
        if (alreadyExists) :
            self.passwordHash = password
            self.passwordSalt = passwordSalt
        else :
            #On créé un salt de taille 8 en utilisant les alphabets ascii
            self.passwordSalt = ''.join((random.choice(string.ascii_letters + string.digits + string.punctuation.replace(':', '')) for i in range(8)))
            #On créé l'objet Hash en sha256
            self.passwordHash = hashes.Hash(hashes.SHA256())
            
            try :
                #On essaye d'encoder la concatenation du mot de passe et du sel
                encodedPassword = (password + self.passwordSalt).encode()
            except UnicodeError:
                #Si on arrive pas a encoder, le message d'erreur pourra être changé
                print("Encodage du mot de passe impossible pour la création de l'utilisateur", name)
                self.passwordHash = None
                return
            
            #On obtien le sha256 du mot de passe et on le transforme en String
            self.passwordHash.update(encodedPassword)
            self.passwordHash = self.passwordHash.finalize().hex()
        

#Permet d'exporter une liste d'utilisateurs dans un fichier de nom filename
#-1 = erreur d'ouverture de fichier
#Renvoie le nombre d'utilisateur exportés dans le fichier sinon
def exportUsers(userList : list, filename : str) :
    try :
        file = open(filename, 'w')
    except OSError:
        print("impossible d'ouvrir le fichier")
        return 1
    
    nbUser=1
    for user in userList :
        if isinstance(user, User) :
            nbUser += 1
            file.write(user.name + ":" + user.passwordHash + ":" + user.passwordSalt + "\n")
    file.close()
    return nbUser

#Permet d'importer une liste d'utilisateurs dans un fichier de nom filename
#-1 = erreur d'ouverture de fichier
#Renvoie la liste des utilisateurs
def importUsers(filename : str) :
    try :
        file = open(filename, 'r')
    except OSError:
        print("impossible d'ouvrir le fichier")
        return 2

    content = file.read()
    content = content.split('\n')

    users = []
    for user in content :
        if (user != "") :
            userContent = user.split(":")
            users.append(User(userContent[0], userContent[1], True, userContent[2]))
    
    file.close()
    return users


#LA FONCTION A UTILISER POUR AJOUTER UN UTILISATEUR / UN ANNUAIRE
#80  Succès
#81 Nom invalide
#82 Mot de passe invalide
#83 User already exists
#84 Username vide
#85 mot de passe vide
#86 Problème encodement
def addUser(username : str, password : str, userList : list) :
    if username == "" :
        return 84
    
    if password == "" :
        return 85

    #Je remet un try except ici. Ceci est redondant, et on pourrais utiliser un raise en ligne 26 et faire un try except de User() ici
    #Malheureusement, je ne sais pas encore bien gérer les raise Exception()
    try :
        #On essaye d'encoder le mot de passe depuis utf-8
        password.encode()
    except UnicodeError:
        return 86

    for user in userList :
        if user.name == username :
            return 81
    
    newUser = User(username, password, False)
    userList.append(newUser)
    annuaire.creerAnnuaire(username)
    
    exportUsers(userList, "passwd.txt")
    return 80

#100  Succès
#102 username invalide
#101 user not found
def removeUser(username : str, userList : list) :
    if username == "" :
        return 102

    for i in range(0, len(userList)) :
        if userList[i].name == username:
            userList.pop(i)
            annuaire.supprimerAnnuaire(username)
            exportUsers(userList, "passwd.txt")
            return 100

    return 101
    
#90  Succès
#1 Nom invalide
#93 Mot de passe invalide
#3 user not found
def changePassword(username : str, password : str, userList : list) :

    if password == "" :
        return 93

    err = removeUser(username, userList)
    if (err != 100) :
        return err
    err = addUser(username, password, userList)
    if (err != 80) :
        return err

    return 90

#Password est le mot de passe à vérifier et on le compare avec passwordHash et passwordSalt
def checkPassword(password : str, passwordHash : str, passwordSalt : str) :
    hashToCheck = hashes.Hash(hashes.SHA256())
    hashToCheck.update((password + passwordSalt).encode())
    hashToCheck = hashToCheck.finalize().hex()

    if (hashToCheck == passwordHash) :
        return True
    return False


def checkPasswordUser(password : str, user : User) :
    return checkPassword(password, user.passwordHash, user.passwordSalt)

def findUser(username : str, userList : list) :
    for user in userList :
        if isinstance(user, User) and user.name == username :
            return user
    return None