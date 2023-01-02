pokedex = []
print("Welcome to your one and only Pokedex! :D \nHere you can create a profile of each pokemon and  be able to track and reaseach that type\n")
print("What would u like todo?\n1. Add a pokemon\n2. Delete a Pokemon\n3. Search for a pokemon\n4. View all Pokemon\n5. Exit the pokedex\n")
while True:
  while True:
    print("")
    choice = input("What would you like todo?: ")
    if choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "5":
      break
    else:
      print("Invalid input >:I .")
  if choice == "1":
    pokemon = []
    added_pokemon = input("What pokemon whould you like to add?: ").lower().strip()
    num = 0
    for i in pokedex:
      if pokedex[num][0] 2== added_pokemon:
        print("Sorry, this is already in your pokedex!")
        num += 1
        break
    typeofpokemon = input("What is the type of this pokemon?: ").lower().strip()
    pokemon.append(added_pokemon)
    pokemon.append(typeofpokemon)
    pokedex.append(pokemon)
  elif choice == "2":
    deleted_pokemon = input("What pokemon whould you like to delete?: ").lower().strip()
    num = 0
    for i in pokedex:
      if pokedex[num][0] == deleted_pokemon:
        pokedex.remove(i)
        break
      num += 1
  elif choice == "3":
    searched_pokemon = input("What pokemon do you want to search for?: ").lower().strip()
    num = 0
    for i in pokedex:
      if pokedex[num][0] == searched_pokemon:
        print("      Pokemon\n---------------")
        print("Name: " + pokedex[num][0])
        print("Type: " + pokedex[num][1])
        num += 1
  elif choice == "4":
    num = 0
    print("     Pokedex")
    for i in pokedex:
        print("---------------")
        print("Name: " + pokedex[num][0])
        print("Type: " + pokedex[num][1])
        num += 1
  elif choice == "5":
    print("Leaving Pokedex. Goodbye :D")
    break