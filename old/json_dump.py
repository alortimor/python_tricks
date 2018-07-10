#!/usr/bin/python3

import json

class Contact:
  def __init__(self, first, last):
    self.first = first
    self.last = last

  @property
  def full_name(self):
    return ("{} {}".format(self.first, self.last))
    
class ContactEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Contact):
      return {'is_contact': True,
              'first': obj.first,
              'last': obj.last,
              'full': obj.full_name}
    return super().default(obj)

def decode_contact(dic):
  if dic.get('is_contact'):
    return Contact(dic['first'], dic['last'])
  else:
    return dic

if __name__ == "__main__":
  c = Contact("Flip", "Flop")
  # print(json.dumps(c.__dict__))
  temp_dic = json.dumps(c, cls=ContactEncoder)
  # d = json.loads(json.dumps(c, cls=ContactEncoder), object_hook=decode_contact) # this will work, but easier to read when a temporary dictionary variable is present
  d = json.loads(temp_dic, object_hook=decode_contact)
  print(d.full_name)
