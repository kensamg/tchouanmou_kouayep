import socket

# Créer un objet socket TCP/IP
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Définir l'adresse IP et le port d'écoute du serveur
adresse_ip = '127.0.0.1'
port = 12345
serveur.bind((adresse_ip, port))

# Mettre le serveur en écoute
serveur.listen(5)

print("Serveur en attente de connexion sur {adresse_ip}:{port}")

while True:
    # Attendre une connexion client
    client, adresse = serveur.accept()
   
    print("Connexion établie avec {adresse[0]}:{adresse[1]}")
   
    # Recevoir les données envoyées par le client
    donnees_recues = client.recv(1024)
    message = donnees_recues.decode('utf-8')
    print("Message reçu: {message}")
   
    # Envoyer une réponse au client
    reponse = "Message bien reçu!"
    client.sendall(reponse.encode('utf-8'))
   
    # Fermer la connexion client
    client.close()