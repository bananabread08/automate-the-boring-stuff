import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)

# connect to server
conn.ehlo()

# for encryption
conn.starttls()

# login
# create an App-specific password in google
conn.login('your_email.gmail.com', 'password')

# send
conn.sendmail('your_email.gmail.com', 'receiver_email@gmail.com','Subject: So long...\n\n Dear Roze')

conn.quit()
