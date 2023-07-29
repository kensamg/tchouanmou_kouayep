import socket

# Créer un objet socket TCP/IP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Définir l'adresse IP et le port du serveur auquel se connecter
adresse_ip = '127.0.0.1'
port = 12345

try:
    # Connecter le client au serveur
    client.connect((adresse_ip, port))
    
    # Envoyer des données au serveur
    message = "Salut serveur b  br!"
    client.sendall(message.encode('utf-8'))
    
    # Recevoir la réponse du serveur
    donnees_recues = client.recv(1024)
    reponse = donnees_recues.decode('utf-8')
    print("Réponse du serveur: {reponse}")
    
finally:
    # Fermer la connexion client
    client.close()