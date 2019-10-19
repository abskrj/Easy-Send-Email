import smtplib, ssl, time
'''
This file takes the SMTP Sender Email address, Receiver Email address as inputs and 
sends a mail with a specific message using GMail as the SMTP server.

This file is useful to send mails from the commandline or programmatically without opening a browser

'''
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
username = 'origin@gmail.com'
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
with smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
