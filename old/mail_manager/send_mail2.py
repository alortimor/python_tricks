#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from collections import defaultdict

def send_email(subject, message, from_addr, *to_addrs, host="localhost", port=1025, **headers):
  email = MIMEText(message)
  email['Subject'] = subject
  email['From'] = from_addr
  
  for header, value in headers.items():
    print("Header - {} Value {}".format(header, value))
    email[header] = value

  sender = smtplib.SMTP(host, port)
  for addr in to_addrs:
    del email['To']
    email['To'] = addr
    sender.sendmail(from_addr, addr, email.as_string())
  sender.quit()

class MailingList:
  def __init__(self):
    self.email_map = defaultdict(set)

  def add_to_group(self, email, group):
    self.email_map[email].add(group) # add element to set

  def emails_in_groups(self, *groups):
    groups = set(groups)
    emails = set()
    for e, g in self.email_map.items():
      if g & groups:
        emails.add(e)
    return emails

  def send_mailing(self, subject, message, from_addr, *groups, headers=None):
    emails = self.emails_in_groups(*groups)
    send_email(subject, message, from_addr, *emails, headers=headers)

if __name__ == "__main__":
  m = MailingList()
  m.add_to_group("friend1@example.com", "friends")
  m.add_to_group("friend2@example.com", "friends")
  m.add_to_group("friend1@example.com", "family")
  m.add_to_group("pro1@example.com", "professional")

  print(m.email_map)
  m.send_mailing("A Party", "Friends and family only: a party", "me@example.com", "friends", "family", headers={"Reply-To": "me2@example.com"})
