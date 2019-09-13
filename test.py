import smtplib, ssl, time

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
