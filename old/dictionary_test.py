#!/usr/bin/python3

favourite_languages = {
  'peter': 'c++',
  'liz': 'java',
  'vincent': 'pl/sql',
  'chris': 'bash',
  'seamus': 'C#',
  'sean': 'pl/sql',
  'allan': 'java'
}

print ("The following languages are listed:")
for language in favourite_languages.values():
	print(language.title())

print ("\nThe following unique languages are listed:")
for language in set(favourite_languages.values()):
	print(language.title())

