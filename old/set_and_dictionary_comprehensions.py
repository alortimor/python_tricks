#!/usr/bin/python3

if __name__ == "__main__":
  from collections import namedtuple

  # sample named tuple
  Book = namedtuple("Book", "author title genre")

  books = [
            Book("Smith", "Time To Die", "Action")
           ,Book("Smith", "Viscious Circle", "Action")
           ,Book("Smith", "Elephant Song", "Action")
           ,Book("Smith", "Rage", "Action")
           ,Book("Smith", "River God", "Action")
           ,Book("Rowling", "The Casual Vacancy", "fantasy")
           ,Book("Rowling", "The Philisopher", "fantasy") 
           ]

  # set comprehension
  fantasy_authors = { b.author for b in books if b.genre in ("Action", "fantasy")}

  print(fantasy_authors)
