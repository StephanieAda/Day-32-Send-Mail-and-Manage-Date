
import smtplib

my_email = "Prinlion265@gmail.com"
password = "Lilyapple123"
dummy_email = "stephanie.hello@yahoo.com"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.ehlo()
    connection.starttls()
    connection.ehlo()
    connection.login(user=my_email, password=password)
    subject = "Hello"
    body = "Its Stephanie"
    connection.sendmail(from_addr=my_email, to_addrs=dummy_email, msg=f"Subject: {subject} \n \n{body}")

