import cmdlet
import UserUtils
import ClientServerClass
import RSAUtils
import time

users = []
users = UserUtils.importUsers("passwd.txt")

currentUser = UserUtils.findUser("Jesse", users)

private, public = RSAUtils.createKeys()

#Création de la connexion
port = input("Veuillez indiquer un port sur lequel le client devra se connecter : ")
try :
    int(port)
except ValueError:
    print("numéro de port invalide, veuillez redémarrer le serveur")
    exit(-1)
serveur = ClientServerClass.Server(int(port))
addr = serveur.start()
if (isinstance(addr, int)) :
    print("Veuillez redémarrer le serveur")
    exit(-1)

print("Synchronisation ...")
time.sleep(1)
print("utilisateur connecté")
#Connexion initiée.

#Securisation connexion avec RSA
print("Envoie de la clé publique")
serveur.send(RSAUtils.publicKeyToPublicBytes(public))
time.sleep(1)
print("Reception de la clé ...")
publicClient = serveur.receiveAll()
publicClient = RSAUtils.publicBytesToPublicKey(publicClient)
print("Clé du client reçue")
time.sleep(1)

serveur.send(RSAUtils.encrypt(b'coucou !', publicClient))




cmd = "quit".split()
while cmd[0] != "quit" :
    
    #cmd = input(">").split(" ")

    if len(cmd) == 2 and cmd[0] == "add" and cmd[1] == "user" :
        if currentUser.name == "root" :
            username = input("Nom de l'utilisateur : ")
            mdp = input("Nouveau mot de passe : ")
            cmdlet.ajouterUserCmd(username, mdp, users)
        else :
            print("Seul l'administrateur peut créer des utilisateurs")

    elif len(cmd) == 2 and cmd[0] == "rm" and cmd[1] == "user" :
        if currentUser.name == "root" :
            username = input("Nom de l'utilisateur : ")
            cmdlet.removeUserCmd(username, users)
        else :
            print("Seul l'administrateur peut supprimer des utilisateurs")

    #J'aime pas avoir autant de if/else embriqué. Mais j'ai ni le choix ni le temps de rafctoriser ce code ci
    if len(cmd) == 2 and cmd[0] == "change" and cmd[1] == "password" :
        if currentUser.name == "root" :
            username = input("Nom de l'utilisateur : ")
            username = UserUtils.findUser(username, users)
            if (username != None) :
                nouveaumdp = input("Nouveau mot de passe : ")
                cmdlet.changePasswordCmd(username, nouveaumdp, users)
            else :
                print("Utilisateur non trouvé ou inexistant")
        else :
            username = currentUser
            mdp = input("Votre ancien mot de passe : ")
            if (UserUtils.checkPasswordUser(mdp, currentUser)) :
                nouveaumdp = input("Nouveau mot de passe : ")
                cmdlet.changePasswordCmd(username, nouveaumdp, users)
                currentUser = UserUtils.findUser(currentUser.name, users)
            else :
                print("Mot de passe invalide")
    
    if len(cmd) == 1 and cmd[0] == "whoami" :
        print(currentUser.name)
    
    if len(cmd) == 2 and cmd[0] == "su":
        user = UserUtils.findUser(cmd[1], users)
        if (user != None) :
            if (currentUser.name == "root") :
                currentUser = user
                print("Changement d'utilisateur effectué avec succès")
            else :
                mdp = input("Mot de passe : ")
                if (UserUtils.checkPasswordUser(mdp, user)) :
                    currentUser = user
                    print("Changement d'utilisateur effectué avec succès")
                else :
                    print("Mot de passe invalide")
        else :
            print("Utilisateur invalide ou inexistant")
    
    if len(cmd) == 2 and cmd[0] == "list" and cmd[1] == "users" :
        for user in users :
            print("-->", user.name)

    if (len(cmd) == 1 or len(cmd) ==2) and cmd[0] == "show" :
        pass
        #TODO montrer