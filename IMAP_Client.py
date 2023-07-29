import imaplib

# Paramètres de connexion
IMAP_SERVER = 'imap.example.com'
USERNAME = 'your_username'
PASSWORD = 'your_password'

# Connexion au serveur IMAP
imap_server = imaplib.IMAP4_SSL(IMAP_SERVER)
imap_server.login(USERNAME, PASSWORD)

# Sélection de la boîte de réception
imap_server.select('INBOX')

# Récupération des IDs des messages présents dans la boîte de réception
status, message_ids = imap_server.search(None, 'ALL')
message_ids = message_ids[0].split()

# Affichage du sujet de chaque message
for message_id in message_ids:
    status, msg_data = imap_server.fetch(message_id, '(RFC822)')
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = response_part[1].decode('utf-8')
            for line in msg.splitlines():
                if line.startswith('Subject:'):
                    subject = line[9:]
                    print('Sujet :', subject)

# Déconnexion du serveur IMAP
imap_server.logout()