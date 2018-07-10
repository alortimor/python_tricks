#!//usr/bin/python3

import user

class AuthException(Exception):
  def __init__(self, user, user=None):
    super().__init__(username, user)
    self.username = username
    self.user = user

class UsernameAlreadyExists(AuthException):
  pass

class PasswordTooShort(AuthException):
  pass

class InvalidUsername(AuthException):
  pass

class InvalidPassword(AuthException):
  pass

