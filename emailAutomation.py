from email import message
import smtplib
import csv

sender_email = "tuf.carwyn@fillnoo.com"

receiver_email = "gabrielbiacchi.gb@gmail.com"

password = "naxgj9Q?"

subject = "Test"

body = "This was sent using Python"

server = smtplib.SMTP('smtp.outlook.com', 587)

server.starttls()

server.login(sender_email, password)


with open("emailautomation\emailstosend.csv", 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        server.sendmail(sender_email, row['emails'], row['codes'])

