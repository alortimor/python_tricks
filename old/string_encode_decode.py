#!/usr/bin/python3

if __name__ == "__main__":
  characters = "cliché"
  print(characters.encode("UTF-8"))

  print(characters.encode("latin-1"))

  print(characters.encode("CP437"))

  # print(characters.encode("ascii")) # this line produces an error since the é character cannot be represented in ascii
  characters = b'\x63\x6c\x69\x63\x68\xe9'
  print(characters)

  
  print(characters.decode("latin-1"))

  characters = b"\x15\xa3"
  # print(characters.decode("UTF-8"))  # generates an error, since \x15\xa3 is not 
