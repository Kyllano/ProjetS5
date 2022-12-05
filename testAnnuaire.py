import ClientServerClass
import sys
import UserUtils
from cryptography.hazmat.primitives import hashes
import string
import AnnuaireUtils


users = []

#test sur l'annuaire pour créer un utilisateur et donc un annuaire
AnnuaireUtils.creerUser(users, "Yon" , "1234")
AnnuaireUtils.creerUser(users, "Pi p", "3.14159265359")
AnnuaireUtils.creerUser(users, "A supprimer", "MdpFacile")
AnnuaireUtils.creerUser(users, "Enzo", "Mdp")
AnnuaireUtils.creerUser(users, "Che", "ikh")

#test pour modifier un annuaire
AnnuaireUtils.modifAnnuaire(users , "Yon" , "1234" , "./users")
#test pour modifier un annuaire mais mauvais mdp
AnnuaireUtils.modifAnnuaire(users, "Pi p", "3,14" , "./users")
AnnuaireUtils.modifAnnuaire(users, "Enzo", "Mdp", "./users")
#test pour supprimer un annuaire avec mdp
AnnuaireUtils.supprUser(users, "A supprimer", "MdpFacile")
AnnuaireUtils.supprUser(users, "Che", "ikh")
#test pour supprimer un annuaire avec mauvais mdp
#AnnuaireUtils.supprUser(users, "A supprimer", "MdpFacil")
#test pour supprimer un annuaire avec mauvaise personne
#AnnuaireUtils.supprUser(users, "A supprime", "MdpFacile")


"""

users = UserUtils.importUsers("passwd.txt")

UserUtils.removeUser("prout", users)

for i in users :
    if isinstance(i, UserUtils.User) :
        print(i.name, i.passwordHash, i.passwordSalt)

print(UserUtils.checkPasswordUser("root", UserUtils.findUser("root", users)))

"""



"""
UserUtils.changePassword("Gus", "POLLOS BROTHA", users)
users.append(UserUtils.User("root", "root", False))
users.append(UserUtils.User("Mr.White", "myPass", False))
users.append(UserUtils.User("Jessy", "IHaveANiceAss", False))
users.append(UserUtils.User("Skyler", "i) [•¡¤¦§¨©ª«¬-®¯±²³¶¹º»¼½¾¿‡•…‪‰‹›⁠⁰€™■･�]", False))

UserUtils.exportUsers(users, "passwd.txt")
"""

"""
passwd = root.password.finalize()
print(passwd)
print(passwd.hex())
"""
