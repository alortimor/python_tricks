#!/usr/bin/python3

file_name='/home/bluefrog/sample_code/python/pi_number.dat'
with open(file_name) as file_object:
  contents = file_object.read()
  print(contents.rstrip())

print('\n')
with open(file_name) as file_object:
  for line in file_object:
    print(line.rstrip())

with open(file_name) as file_object:
  lines = file_object.readlines()

print('\n')
for line in lines:
  print(line.rstrip())

pi_string = ''
for line in lines:
  pi_string += line.strip()

print('\n')
print(pi_string)
print(len(pi_string))
