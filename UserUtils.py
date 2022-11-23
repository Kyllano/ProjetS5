from cryptography.hazmat.primitives import hashes
import random
import string


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
            self.passwordSalt = ''.join((random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(8)))
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
        return -1
    
    nbUser=0
    for user in userList :
        if isinstance(user, User) :
            nbUser += 1
            file.write(user.name + ":" + user.passwordHash + ":" + user.passwordSalt + "\n")
    file.close()
    return nbUser

def importUsers(filename : str) :
    try :
        file = open(filename, 'r')
    except OSError:
        print("impossible d'ouvrir le fichier")
        return -1

    content = file.read()
    content = content.split('\n')

    users = []
    for user in content :
        if (user != "") :
            userContent = user.split(":")
            users.append(User(userContent[0], userContent[1], True, userContent[2]))
    
    file.close()
    return users