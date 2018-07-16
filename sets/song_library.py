#!/usr/bin/python3

song_library = [("Phantom Of The Opera", "Sarah Brightman"),
                ("Knocking On Heaven's Door", "Guns N' Roses"),
                ("Captain Nemo", "Sarah Brightman"),
                ("Patterns In The Ivy", "Opeth"),
                ("November Rain", "Guns N' Roses"),
                ("Beautiful", "Sarah Brightman"),
                ("Mal's Song", "Vixy and Tony")]

# when using curly brackets without using colon, the result is a set, not a dictionary
play_list_artists = {"Juluka", "Guns N' Roses", "Vixy and Tony", "Savuka"}

sa_artists = {"Juluka", "Savuka"}

if __name__ == "__main__":
  artists = set()
  for song, artist in song_library:
    artists.add(artist)

  print(artists)

  print("All {}".format(artists.union(play_list_artists)))
  print("Both {}".format(artists.intersection(play_list_artists)))
  print("Either, but no both {}".format(artists.symmetric_difference(play_list_artists)))

  print("Is subset {}".format(sa_artists.issubset(play_list_artists)))
