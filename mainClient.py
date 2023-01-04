import ClientServerClass
import RSAUtils
import time

private, public = RSAUtils.createKeys()
isAuthenticated = False
currentUser = None


#TODO GET CLIENT
client = ClientServerClass.Client(2222, "127.0.0.1")


client.connect()
print("client connecté !")
print("Reception de la clé...")
publicServer = client.receiveAll()
publicServer = RSAUtils.publicBytesToPublicKey(publicServer)
print("Clé du server reçue")
#time.sleep(1)
print("envoie clé client")
client.send(RSAUtils.publicKeyToPublicBytes(public))


while (not isAuthenticated) :
    username = input("Veuillez indiquer votre identifiant : ")
    mdp = input("Veuillez indiquer votre mot de passe : ")

    if (username != "" and mdp != "") :
        credentials = username + " " + mdp
        client.send(RSAUtils.encrypt(credentials.encode(), publicServer))
        reponse = RSAUtils.decrypt(client.receiveAll(), private)
        reponse = int.from_bytes(reponse, 'little')
        print(reponse)
        match (reponse) :
            case 0:
                isAuthenticated = True
                currentUser = username
                print("succes")
            case -1:
                print("identifiants invalides ou inexistants")
            case -2 :
                print("utilisateur inexistant")
    else :
        print("Identifiants invalide")



cmd = [None]
while cmd[0] != "logout" :
    
    cmd = input(">").split(" ")

    if len(cmd) == 2 and cmd[0] == "add" and cmd[1] == "user" :
        username = input("Nom de l'utilisateur : ")
        mdp = input("Nouveau mot de passe : ")
        cmdserv = "add user " + username + " " + mdp

        print("on envoie :", cmdserv)

        client.send(RSAUtils.encrypt(cmdserv.encode(), publicServer))
        reponse = RSAUtils.decrypt(client.receiveAll(), private)
        reponse = int.from_bytes(reponse, 'little')

        #TODO afficher erreur POUR TOUTES LES FONCTIONS
        print("RETOUR :", reponse)
        

    elif len(cmd) == 2 and cmd[0] == "rm" and cmd[1] == "user" :
        username = input("Nom de l'utilisateur : ")
        cmdserv = "rm user " + username

        client.send(RSAUtils.encrypt(cmdserv.encode(), publicServer))
        reponse = RSAUtils.decrypt(client.receiveAll(), private)
        reponse = int.from_bytes(reponse, 'little')

        #TODO afficher erreur POUR TOUTES LES FONCTIONS
        print("RETOUR :", reponse)

    #J'aime pas avoir autant de if/else embriqué. Mais j'ai ni le choix ni le temps de rafctoriser ce code ci
    if len(cmd) == 2 and cmd[0] == "change" and cmd[1] == "pass" :
        if currentUser == "root" :
            username = input("Nom de l'utilisateur : ")
            nouveaumdp = input("Nouveau mot de passe : ")
            oldmdp = "blank"
        else :
            username = currentUser
            oldmdp = input("Votre ancien mot de passe : ")
            nouveaumdp = input("Votre nouveau mot de passe")
        cmdserv = "change pass "+ username + " " + nouveaumdp + " " + oldmdp

        client.send(RSAUtils.encrypt(cmdserv.encode(), publicServer))
        reponse = RSAUtils.decrypt(client.receiveAll(), private)
        reponse = int.from_bytes(reponse, 'little')


        print("RETOUR :", reponse)


    if len(cmd) == 1 and cmd[0] == "whoami" :
        cmdserv = "whoami"
        client.send(RSAUtils.encrypt(cmdserv.encode(), publicServer))
        reponse = RSAUtils.decrypt(client.receiveAll(), private).decode()
        print(reponse)
    
    if len(cmd) == 2 and cmd[0] == "list" and cmd[1] == "users" :
        cmdserv = "list users"
        client.send(RSAUtils.encrypt(cmdserv.encode(), publicServer))
        reponse = RSAUtils.decrypt(client.receiveAll(), private).decode()
        print(reponse)

    #su user
    if len(cmd) == 2 and cmd[0] == "su":
        if (currentUser == "root") :
            cmdserv = "su "+ cmd[1] +" blank"
        else :
            mdp = input("Mot de passe : ")
            cmdserv = "su " + cmd[1] + " " + mdp
        
        client.send(RSAUtils.encrypt(cmdserv.encode(), publicServer))
        reponse = RSAUtils.decrypt(client.receiveAll(), private)
        reponse = int.from_bytes(reponse, 'little')
        if (reponse == 0) :
            currentUser = cmd[1]
        print(reponse)

    if (len(cmd) == 1 or len(cmd) == 2) and cmd[0] == "show" :
        if len(cmd) == 2 :
            user = cmd[1]
        else :
            user = currentUser
        cmdserv = "show " + user
        client.send(RSAUtils.encrypt(cmdserv.encode(), publicServer))
        reponse = RSAUtils.decrypt(client.receiveAll(), private)
        reponse = int.from_bytes(reponse, 'little')
        print(reponse)

        if (reponse == 0) :
            nbContacts = RSAUtils.decrypt(client.receiveAll(), private)
            nbContacts = int.from_bytes(nbContacts, 'little')
            print("j'ai recu ", nbContacts)

            print("Annuaire de ", user)
            for i in range(0, nbContacts) :
                recu = client.receive256()
                #print("RECU \n :", recu)
                recu = RSAUtils.decrypt(recu, private).decode()
                print(recu)
                print("Je recois contacte")
    
    print("JAI EU LE TEMPS DE FINIR")


            






    if len(cmd) == 1 and cmd[0] == "logout" :
        print("deconnexion client")
        client.send(RSAUtils.encrypt(cmd[0].encode(), publicServer))
        client.closeConnection()
