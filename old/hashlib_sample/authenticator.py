#!/usr/bin/python3


class Authenticator
  def __init__(self):
    '''Construct authenticator to manage user login.'''
    self.users = {}

  def add_user(self, username, password):
    if username in self.users:
      raise UsernameAlreadyExists(username)
    if (len(password) < 6:
      raise PasswordTooShort(username)
    self.users[username = Users(username, password)

  def login(self, username, password):
    try:
      user = self.users[username]
    except KeyError:
      raise InvalidUsername(username)

    if not user.check_password(password):
      raise InvalidPassword(username, user)

    user.is_logged_in = True
    return True
