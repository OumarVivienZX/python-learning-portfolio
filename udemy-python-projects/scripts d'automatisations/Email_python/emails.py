import emails_config
import smtplib
from email.mime.multipart import MIMEMultipart#Importation de la classe MIMEMultipart pour créer des messages multipart (texte, HTML, pièces jointes, etc.)
from email.mime.text import MIMEText#Importation de la classe MIMEText pour créer des messages texte
#Envoyer des Emails
#Implémentation

def envoyer_email(email_destinataire, sujet, message) :

    multipart_message = MIMEMultipart()#Création d'un message multipart qui peut contenir du texte, du HTML, des pièces jointes, etc.
    multipart_message['Subject'] = sujet
    multipart_message['From'] = emails_config.config_email
    multipart_message['To'] = email_destinataire
    multipart_message.attach(MIMEText(message, 'plain'))#Attacher le message texte au message multipart
    server_mail = smtplib.SMTP(emails_config.config_server, emails_config.config_server_port)#Connexion au serveur SMTP
    server_mail.starttls()#Démarrer la connexion sécurisée TLS
    server_mail.login(emails_config.config_email, emails_config.config_password)#Authentification auprès du serveur SMTP
    server_mail.sendmail(emails_config.config_email, email_destinataire, multipart_message.as_string())#Envoyer l'email
    server_mail.quit()

message_email = "Bonjour, ceci est un test d'envoi d'email depuis Python !"
envoyer_email("xxxx@gmail.com","Email depuis python", message_email)

# - starttls() → sécuriser la connexion avec TLS.
# - login(email, password) → s’authentifier.
# - sendmail(from, to, message) → envoyer l’email.
# - quit() → fermer la connexion.
