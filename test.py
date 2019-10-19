import ssl, time
import mimetypes
import os
import smtplib

from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#this item add the attachment to email 

def add_attachment(msg, filename):
    if not os.path.isfile(filename):
        return

    ctype, encoding = mimetypes.guess_type(filename)

    if ctype is None or encoding is not None:
        ctype = 'application/octet-stream'

    maintype, subtype = ctype.split('/', 1)

    if maintype == 'text':
        with open(filename) as f:
            mime = MIMEText(f.read(), _subtype=subtype)
    elif maintype == 'image':
        with open(filename, 'rb') as f:
            mime = MIMEImage(f.read(), _subtype=subtype)
    elif maintype == 'audio':
        with open(filename, 'rb') as f:
            mime = MIMEAudio(f.read(), _subtype=subtype)
    else:
        with open(filename, 'rb') as f:
            mime = MIMEBase(maintype, subtype)
            mime.set_payload(f.read())

        encoders.encode_base64(mime)

    mime.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(mime)

'''
This file takes the SMTP Sender Email address, Receiver Email address as inputs and 
sends a mail with a specific message using GMail as the SMTP server.

This file is useful to send mails from the commandline or programmatically without opening a browser

'''
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "" # Enter sender's email
receiver_email = " "  # Enter receiver address
password = " " #Enter sender's pass
date = time.ctime()
message = """\
Subject: [Web Development Course Reminder]

This message is sent because you have took oath that you will study daily web development. So, start now.
Current Time/Date: {date}
--Abhishek Raj
--Naam to suna hi hoga."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
