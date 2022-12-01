def validContact(ID : int , nom : str , prenom :  str , email : str) :
    if((ID == 0) or (len(nom) == 0) or (len(prenom) == 0) or (len(email) == 0)):
        print("#Caractere obligatoire vide")
        return -2 #Carractere obligatoire vide
    elif(not((isinstance (ID, int)) and (isinstance (nom, str)) and (isinstance (prenom, str)) and (isinstance (email, str)))):
        print("#Caractère obligatoire invalide")
        return -1 #Carractère obligatoire invalide
    else : 
        print("#Caractère valide")
        return 1 #Contact valide