#!/usr/bin/python3


from format_name import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
  first = input("\nEnter first name: ")
  if (first == 'q'):
    break
  last = input("Enter last name: ")
  if (last == 'q'):
    break
  formatted_name = get_formatted_name(first,last)
  print("Formatted name : " + formatted_name)

