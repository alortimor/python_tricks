#!/usr/bin/python3

class Authorizor:
  def __init__(self, authenticator):
    self.authenticator = authenticator
    self.permissions = {}

  def add_permission(self, perm_name):
     '''Create a new permission that users can be added to.'''
     try:
       perm_set = sef.permissions[perm_name]
    except KeyError:
      self.permissions[perm_name = set()
    else:
      
