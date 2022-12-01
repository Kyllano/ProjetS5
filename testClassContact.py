import utils

#Test contact vide
utils.validContact(1,'Yon','','mail')

#Test contact mal renseignée
utils.validContact("gyff","Yon","BEAURAIN","email@gmail.com")

#Test bon contact
utils.validContact(3 , "Yon" , "BEAURAIN" , "email")
