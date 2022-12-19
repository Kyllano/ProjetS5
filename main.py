import cmdlet
import UserUtils

users = []
users = UserUtils.importUsers("passwd.txt")

currentUser = users[0]

cmd = input(">").split(" ")

if cmd[0] == "add" and cmd[1] == "user" :
    username = input("Nom de l'utilisateur : ")
    mdp = input("Nouveau mot de passe : ")
    cmdlet.ajouterUserCmd(username, mdp, users)

if cmd[0] == "rm" and cmd[1] == "user" :
    username = input("Nom de l'utilisateur : ")
    cmdlet.removeUserCmd(username, users)

if cmd[0] == "change" and cmd[1] == "password" :
    pass
