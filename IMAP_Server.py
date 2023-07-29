import imaplib

# Paramètres de connexion
IMAP_SERVER = 'imap.example.com'
USERNAME = 'your_username'
PASSWORD = 'your_password'

# Connexion au serveur IMAP
imap_server = imaplib.IMAP4(IMAP_SERVER)
imap_server.login(USERNAME, PASSWORD)

# Liste de tous les dossiers (boîtes aux lettres) disponibles
response, folders = imap_server.list()
print(folders)

# Sélection d'une boîte aux lettres
response, mailbox = imap_server.select('INBOX')
print(mailbox)

# Recherche des e-mails dans la boîte aux lettres
response, message_ids = imap_server.search(None, 'ALL')
message_id_list = message_ids[0].split()
print("Nombre d'e-mails trouvés : {len(message_id_list)}")

# Récupération du contenu de chaque e-mail
for message_id in message_id_list:
    response, message_data = imap_server.fetch(message_id, '(RFC822)')

    # Le message est stocké dans message_data[0][1]
    print(message_data[0][1])

# Déconnexion du serveur IMAP
imap_server.logout()

