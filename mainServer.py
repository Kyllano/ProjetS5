import UserUtils
import ClientServerClass
import RSAUtils
import time
import annuaire
import retours

users = []
users = UserUtils.importUsers("passwd.txt")

currentUser = None

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


#time.sleep(1)
print("Connexion entrante")
#Connexion initiée.


print("Echange de cle RSA")
#Securisation connexion avec RSA
#print("Envoie de la clé publique")
serveur.send(RSAUtils.publicKeyToPublicBytes(public))
#time.sleep(1)
#print("Reception de la clé ...")
publicClient = serveur.receiveAll()
publicClient = RSAUtils.publicBytesToPublicKey(publicClient)
#print("Clé du client reçue")
#Echange de clé effectué

#Authentification
print("\nAuthentification : ")
retour = None
while (currentUser == None or retour != 10) :
    credentials = RSAUtils.decrypt(serveur.receiveAll(), private).decode()
    credentials = credentials.split(" ")
    if (UserUtils.findUser(credentials[0], users)) :
        user = UserUtils.findUser(credentials[0], users)
        if (UserUtils.checkPasswordUser(credentials[1], user)) :
            currentUser = user
            retour = 10
        else :
            retour = 11
    else :
        retour = 12
    serveur.send(RSAUtils.encrypt(retour.to_bytes(5, 'little'), publicClient))

retours.analyseCodesRetours(retour)





cmd = [None]
while cmd[0] != "logout" :
    cmd = RSAUtils.decrypt(serveur.receiveAll(), private).decode().split(" ")


    #ADD USER [NOM] [PASS]
    if len(cmd) == 4 and cmd[0] == "add" and cmd[1] == "user" :
        if currentUser.name == "root" :
            username = cmd[2]
            password = cmd[3]
            retour = UserUtils.addUser(username, password, users)
        else :
            retour = 83
        #On envoie le retour d'erreur
        serveur.send(RSAUtils.encrypt(retour.to_bytes(5, 'little'), publicClient))


    #RM USER [NOM]
    elif len(cmd) == 3 and cmd[0] == "rm" and cmd[1] == "user" :
        if currentUser.name == "root" :
            username = cmd[2]
            retour = UserUtils.removeUser(username, users)
        else :
            retour = 103
        serveur.send(RSAUtils.encrypt(retour.to_bytes(5, 'little'), publicClient))
        

    #CHANGE PASS USER NEW OLD
    if len(cmd) == 5 and cmd[0] == "change" and cmd[1] == "pass" :
        if currentUser.name == "root" :
            user = cmd[2]
            user = UserUtils.findUser(user, users)
            if (user != None) :
                nouveaumdp = cmd[3]
                retour = UserUtils.changePassword(user.name, nouveaumdp, users)
            else :
                retour = 91
        else :
            user = currentUser
            mdp = cmd[4]
            if (UserUtils.checkPasswordUser(mdp, currentUser)) :
                nouveaumdp = cmd[3]
                retour = UserUtils.changePassword(user.name, nouveaumdp, users)
                currentUser = UserUtils.findUser(currentUser.name, users)
            else :
                retour = 92
        serveur.send(RSAUtils.encrypt(retour.to_bytes(5, 'little'), publicClient))
       
    #WHOAMI
    if len(cmd) == 1 and cmd[0] == "whoami" :
        serveur.send(RSAUtils.encrypt(currentUser.name.encode(), publicClient))
    
    #LIST USERS
    if len(cmd) == 2 and cmd[0] == "list" and cmd[1] == "users" :
        reponse = ""
        for user in users :
            reponse += "-->" + user.name +"\n"
        serveur.send(RSAUtils.encrypt(reponse[0:-1].encode(), publicClient))

    #SU USER MDP
    if len(cmd) == 3 and cmd[0] == "su":
        user = UserUtils.findUser(cmd[1], users)
        if (user != None) :
            if (currentUser.name == "root") :
                currentUser = user
                retour = 110
            else :
                mdp = cmd[2]
                if (UserUtils.checkPasswordUser(mdp, user)) :
                    currentUser = user
                    retour = 110
                else :
                    retour = 111
        else :
            retour = 112
        serveur.send(RSAUtils.encrypt(retour.to_bytes(5, 'little'), publicClient))
    
    #SHOW USER
    if len(cmd) == 2 and cmd[0] == "show" :
        user = UserUtils.findUser(cmd[1], users)
        if (user != None) :
            ann = annuaire.importAnnuaire(user.name)
            #Si l'utilisateur a les droits
            if(currentUser.name in ann.userRights or currentUser.name == "root") :
                retour = 20
            else :
                retour = 21
        else :
            retour = 22
        
        serveur.send(RSAUtils.encrypt(retour.to_bytes(5, 'little'), publicClient))

        if retour == 20 :
            nbContact = len(ann.contacts)
            print("NbContact : " , nbContact)
            time.sleep(1)
            serveur.send(RSAUtils.encrypt(nbContact.to_bytes(5, 'little'), publicClient))

            print("Envoie de l'annuaire de", user.name)
            for c in ann.contacts :
                tosend = c[0]+ " " + c[1]+ " " + c[2]+ " " +c[3]+ " " + c[4]+ " " + c[5]
                time.sleep(0)
                mess = RSAUtils.encrypt(tosend.encode(), publicClient)
                serveur.send(mess)

    #ADD CONTACT NOM PRENOM MAIL ADDRESSE PORTABLE
    if len(cmd) == 7 and cmd[0] == "add" and cmd[1] == "contact" :
        retour = annuaire.addContact(currentUser.name, cmd[2], cmd[3], cmd[4], cmd[5], cmd[6])
        serveur.send(RSAUtils.encrypt(retour.to_bytes(5, 'little'), publicClient))

    #RM CONTACT ID
    if len(cmd) == 3 and cmd[0] == "rm" and cmd[1] == "contact" :
        retour = annuaire.removeContact(currentUser.name, int(cmd[2]))
        serveur.send(RSAUtils.encrypt(retour.to_bytes(5, 'little'), publicClient))

    #ADD RIGHT USERNAME
    if len(cmd) == 3 and cmd[0] == "add" and cmd[1] == "right" :
        user = UserUtils.findUser(cmd[2], users)
        if (user != None) :
            retour = annuaire.addRightsAnnuaires(currentUser.name, cmd[2])
        else :
            retour = 61

        serveur.send(RSAUtils.encrypt(retour.to_bytes(5, 'little'), publicClient))


    #RM RIGHT USERNAME
    if len(cmd) == 3 and cmd[0] == "rm" and cmd[1] == "right" :
        user = UserUtils.findUser(cmd[2], users)
        if (user != None) :
            retour = annuaire.removeRightsAnnuaires(currentUser.name, cmd[2])
        else :
            retour = 68

        serveur.send(RSAUtils.encrypt(retour.to_bytes(5, 'little'), publicClient))
        

    #LOGOUT
    if len(cmd) == 1 and cmd[0] == "logout" :
        print("deconnexion serveur")
        serveur.closeConnection()