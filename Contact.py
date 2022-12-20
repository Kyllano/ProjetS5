def Ajouter_contact(nom,prenom,email,numtel,adresse):
    Id = 0
    file = open("./Contacts.txt" ,"a+")
    file.close()
    file = open("./Contacts.txt", "r")
    leng = len(file.readlines())
    file.close()
    file = open("./Contacts.txt" ,"a+")
    if leng != 0:
        Id = leng
    Id = Id + 1
    contact = str(Id) + ";" + nom + ";" + prenom + ";" + email + ";" + numtel + "," + adresse + "\n"
    file.write(contact)



    # test
def Modifier_contact(id,nom,prenom,email,numtel,adresse):
    file = open("./Contacts.txt" ,"r")
    lines = file.readlines()
    file.close()
    lines[id-1] = str(id) + ";" + nom + ";" + prenom + ";" + email + ";" + numtel + "," + adresse + "\n"
    file = open("./Contacts.txt" ,"w")
    file.writelines(lines)
    file.close
