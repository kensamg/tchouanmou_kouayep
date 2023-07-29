import socket

# Paramètres de connexion
HOST = 'localhost'
PORT = 8888

# Création du socket du serveur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print('Le serveur écoute sur le port', PORT)

# Attente de la connexion d'un client
client_socket, address = server_socket.accept()
print('Client connecté :', address)

# Réception et traitement des données du client
while True:
    data = client_socket.recv(1024).decode('utf-8')
    if not data:
        break
    print('Données reçues du client :', data)


# Fermeture des connexions
client_socket.close()
server_socket.close()