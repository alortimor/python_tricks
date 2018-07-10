
#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText

def send_email(subject, message, from_addr, *to_addrs, host="localhost", port=1025, **headers):
  email = MIMEText(message)
  email['Subject'] = subject
  email['From'] = from_addr
  for header, value in headers.items():
    email[header] = value

  sender = smtplib.SMTP(host, port)
  for addr in to_addrs:
    del email['To']
    email['To'] = addr
    sender.sendmail(from_addr, addr, email.as_string())
  sender.quit()

if __name__ == "__main__":
  # headers = {}
  send_email("A model subject", "The message contents", "from@example.com", "to1@example.com", "to2@example.com", "Reply-To", "me2@example.com")
