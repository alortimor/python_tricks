#!/usr/bin/python3

if __name__ == "__main__":
  input_strings = ['1', '5', '44', '32', '2', '900']

  output_integers = [int(num) for num in input_strings]
  print(output_integers)
  output_integers = [int(num) for num in input_strings if len(num) < 3]
  print(output_integers)
  
