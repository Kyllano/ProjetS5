import ClientServerClass
import RSAUtils
import ClientServerClassUtils
import retours

private, public = RSAUtils.createKeys()
isAuthenticated = False
currentUser = None


port = input("Veuillez indiquer un port le client se connectera : ")
addresse = input("Veuillez indiquer l'adresse à laquelle le client se connectera : ")
try :
    int(port)
except ValueError:
    print("numéro de port invalide, veuillez redémarrer le client")
    exit(-1)
if (not ClientServerClassUtils.checkValidIpAddress(addresse) ) :
    print("Veuillez indiquer une adresse IPv4 valide")
    exit(-1)
client = ClientServerClass.Client(int(port), "127.0.0.1")


client.connect()
print("Connexion effectuée ! ")
print("Echange de clé")
#print("client connecté !")
#print("Reception de la clé...")
publicServer = client.receiveAll()
publicServer = RSAUtils.publicBytesToPublicKey(publicServer)
#print("Clé du server reçue")
#time.sleep(1)
#print("envoie clé client")
client.send(RSAUtils.publicKeyToPublicBytes(public))


while (not isAuthenticated) :
    username = input("Veuillez indiquer votre identifiant : ").replace(" ", "_")
    mdp = input("Veuillez indiquer votre mot de passe : ").replace(" ", "_")

    if (username != "" and mdp != "") :
        credentials = username + " " + mdp
        client.send(RSAUtils.encrypt(credentials.encode(), publicServer))
        reponse = RSAUtils.decrypt(client.receiveAll(), private)
        reponse = int.from_bytes(reponse, 'little')
        print(reponse)
        match (reponse) :
            case 10:
                isAuthenticated = True
                currentUser = username
                print("succes")
            case 11:
                print("identifiants invalides ou inexistants")
            case 12 :
                print("utilisateur inexistant")
    else :
        print("Identifiants invalide")



cmd = [None]
while cmd[0] != "logout" :
    
    cmd = input(">").split(" ")

    if len(cmd) == 1 and cmd[0] == "help" :
        print("Les commandes possibles sont les suivantes :")
        print(">>logout\nPermet de se deconnecter")
        print(">>show [username]\nPermet d'afficher l'annuaire d'un utilisateur. Si [username] n'est pas renseigné, on utilisera l'utilisateur connecté")
        print(">>list users\nPermet de connaitre l'identité des utilisateurs existants")
        print(">>whoami\nPermet de connaitre l'identité de l'utilisateur connecté")
        print(">>change pass\nPermet de changer le mot de passe de l'utilisateur connecté")
        print(">>add right [username]\nPermet d'ajouter les droits de lecture de son annuaire à un utilisateur")
        print(">>rm right [username]\nPermet de supprimer les droits de lecture de son annuaire à un utilisateur")
        print(">>su [nom d'utilisateur]\nPermet de changer de compte utilisateur")
        print(">>add user\nPermet à l'utilisateur root d'ajouter un utilisateur")
        print(">>rm user\nPermet à l'utilisateur root de supprimer un utilisateur")
        

    if len(cmd) == 2 and cmd[0] == "add" and cmd[1] == "user" :
        username = input("Nom de l'utilisateur : ").replace(" ", "_")
        mdp = input("Nouveau mot de passe : ").replace(" ", "_")
        cmdserv = "add user " + username + " " + mdp

        client.send(RSAUtils.encrypt(cmdserv.encode(), publicServer))
        reponse = RSAUtils.decrypt(client.receiveAll(), private)
        reponse = int.from_bytes(reponse, 'little')

        retours.analyseCodesRetours(reponse)

        

    elif len(cmd) == 2 and cmd[0] == "rm" and cmd[1] == "user" :
        username = input("Nom de l'utilisateur : ")
        cmdserv = "rm user " + username

        client.send(RSAUtils.encrypt(cmdserv.encode(), publicServer))
        reponse = RSAUtils.decrypt(client.receiveAll(), private)
        reponse = int.from_bytes(reponse, 'little')
       
        retours.analyseCodesRetours(reponse)


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
       
        retours.analyseCodesRetours(reponse)


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
    #attention ! ecrire dans le help que les espace doivent etre remplacé par des _
    if len(cmd) == 2 and cmd[0] == "su":
        if (currentUser == "root") :
            cmdserv = "su "+ cmd[1] +" blank"
        else :
            mdp = input("Mot de passe : ")
            cmdserv = "su " + cmd[1] + " " + mdp
        
        client.send(RSAUtils.encrypt(cmdserv.encode(), publicServer))
        reponse = RSAUtils.decrypt(client.receiveAll(), private)
        reponse = int.from_bytes(reponse, 'little')
        if (reponse == 110) :
            currentUser = cmd[1]

        retours.analyseCodesRetours(reponse)

    #show
    if (len(cmd) == 1 or len(cmd) == 2) and cmd[0] == "show" :
        if len(cmd) == 2 :
            user = cmd[1]
        else :
            user = currentUser
        cmdserv = "show " + user
        client.send(RSAUtils.encrypt(cmdserv.encode(), publicServer))
        reponse = RSAUtils.decrypt(client.receiveAll(), private)
        reponse = int.from_bytes(reponse, 'little')

        if (reponse == 20) :
            nbContacts = RSAUtils.decrypt(client.receiveAll(), private)
            nbContacts = int.from_bytes(nbContacts, 'little')
            #print("j'ai recu ", nbContacts)

            print("Annuaire de ", user, ":")
            for i in range(0, nbContacts) :
                recu = RSAUtils.decrypt(client.receive256(), private).decode()
                #Efectuer affichage propre
                print(recu)
        else :
            retours.analyseCodesRetours(reponse)
    

    if len(cmd) == 2 and cmd[0] == "add" and cmd[1] == "contact" :
        nom = input("Nom : ").replace(" ", "_")
        prenom = input("Prenom : ").replace(" ", "_")
        mail = input("Mail : ").replace(" ", "_")
        addresse = input("Addresse : ").replace(" ", "_")
        tel = input("Numero de Telephone : ").replace(" ", "_")
        if (nom == "" or prenom == "" or mail == "") :
            print("Le contacte doit avoir au moins un nom, prenom et mail valide")
        else :
            cmdserv = "add contact " + nom + " " + prenom + " " + mail + " " + addresse + " " + tel
            
            client.send(RSAUtils.encrypt(cmdserv.encode(), publicServer))
            reponse = RSAUtils.decrypt(client.receiveAll(), private)
            reponse = int.from_bytes(reponse, 'little')

            retours.analyseCodesRetours(reponse)


    if len(cmd) == 3 and cmd[0] == "rm" and cmd[1] == "contact" :
        if (RSAUtils.isdigit(cmd[2])) :
            cmdserv = "rm contact " + cmd[2]
            client.send(RSAUtils.encrypt(cmdserv.encode(), publicServer))
            reponse = RSAUtils.decrypt(client.receiveAll(), private)
            reponse = int.from_bytes(reponse, 'little')

            retours.analyseCodesRetours(reponse)
        else :
            print("L'ID de contact fournit n'existe pas")
        
    if len(cmd) == 3 and cmd[0] == "add" and cmd[1] == "right" :
        cmdserv = "add right " + cmd[2]
        client.send(RSAUtils.encrypt(cmdserv.encode(), publicServer))
        reponse = RSAUtils.decrypt(client.receiveAll(), private)
        reponse = int.from_bytes(reponse, 'little')
        
        retours.analyseCodesRetours(reponse)

    if len(cmd) == 3 and cmd[0] == "rm" and cmd[1] == "right" :
        cmdserv = "rm right " + cmd[2]
        client.send(RSAUtils.encrypt(cmdserv.encode(), publicServer))
        reponse = RSAUtils.decrypt(client.receiveAll(), private)
        reponse = int.from_bytes(reponse, 'little')
        
        retours.analyseCodesRetours(reponse)



    if len(cmd) == 1 and cmd[0] == "logout" :
        print("deconnexion client")
        client.send(RSAUtils.encrypt(cmd[0].encode(), publicServer))
        client.closeConnection()
