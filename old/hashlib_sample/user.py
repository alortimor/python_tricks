#!//usr/bin/python3

import hashlib

class User:
  def __init__(self, username, password):
    '''Create a new object. Password encrypted before storing.'''

    self.username = username
    self.password = self._encrypt_pw(password)
    self.is_logged_in = False

  def _encrypt_pw(self, password):
    '''Encrypt password and string and return hash.'''
    hash_string = (self.username + self.password)
    hash_string = hash_string.encode("utf8")
    return hashlib.sha256(hash_string).hexdigest()

  def check_password(self, password):
    '''Return True if password is valid for user.'''
    encrypted = self._encypt_pw(password)
    return encrypted == self.password

