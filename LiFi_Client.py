import socket

# Paramètres de connexion
HOST = 'localhost'
PORT = 8888

# Création du socket du client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur LiFi
client_socket.connect((HOST, PORT))
print('Connecté au serveur LiFi sur', HOST, ':', PORT)

# Envoie de données au serveur
data = "Données à envoyer au serveur LiFi"
client_socket.sendall(data.encode('utf-8'))
print('Données envoyées au serveur LiFi :', data)

# Fermeture de la connexion
client_socket.close()
