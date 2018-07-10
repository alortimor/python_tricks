#!/usr/bin/python3

class UserQuitError(Exception):
  pass

def input_with_quit(prompt):
  user_input = input(prompt)
  if user_input.lower() == "q":
      raise UserQuitError
  return user_input 

if __name__ == "__main__":
  try:
      p = input_with_quit("Enter pattern (q to quit): ") 
      s = input_with_quit("Enter string (q to quit): ")
      print (s, p)
  except UserQuitError:
      print("Have a nice day!") 
