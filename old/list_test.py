#!/usr/bin/python3

test_list = ['pizza','burger','chips','steak']

for food in test_list:
  print("Junk food item is : " + food)


test_dictionary = {'pizza': ['dough','pepperoni','mushrooms'],
                  'burger': ['meat','bread']
                  }

for key, value in test_dictionary.items():
  print("Junk food item is : " + key)
  print ("Ingredients are : ")
  for ingredient in value:
    print(ingredient)



