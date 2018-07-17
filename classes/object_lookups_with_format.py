#!/usr/bin/python3

class EMail:
  def __init__(self, from_addr, to_addr, subject, message):
    self.from_addr = from_addr
    self.to_addr = to_addr
    self.subject = subject
    self.message = message



if __name__ == "__main__":
  email = EMail("p1@example.com", "p2@example.com", "You have mail!", "Test message")

  template = """
  From <{0.from_addr}>
  To: <{0.to_addr}>
  Subject: {0.subject}
  
  {0.message}"""

  print(template.format(email))
