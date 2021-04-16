import socket

   host = 'localhost'
   port = 80

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try :
    serversocket.bind((socket.gethostname(), 80))

except socket.error :
   print("le serveur n'a pas lancée")
   exit()

   serversocket.listen(5)
   print("le serveur est mis en route")

   continuer = True

while True :
   connexion, adresse = serversocket.accept()
   ct = client_thread(clientsocket)
    ct.run()

   print("une personne est connecter avec pour ip {0} et pour port {1}".format(adresse[0], adresse[1]))
