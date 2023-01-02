## ETSEA Adventure Game

#restart = "yes"
#while restart == "yes":

# Welcomes User
adventurer = input("Hello! What is your name? ")
print("Welcome to our game, {}.".format(adventurer))

# HP
hp = 100
print("You have 100 HP, if it gets to 0, you will die! So be careful!")

# Game Begin.
while True:
  pathway = input("Now choose a path 🗺️ ! \n Will you go left or right? ").lower()

  if pathway == "left":
    print("You see a sword. You pick it up. You now have a large wooden pointy stick 🗡. ")
    weapon = 1
    #so we know what text to use
    break

  elif pathway == "right" :
    print("You see a wizards staff 🧙‍♂️. You pick it up. You now have a long splinter that explodes stuff. ")
    weapon = 2
    #so we know what text to use
    break
    
  else:
    print("This is an invalid option.")
  
print("You suddenly encounter a large beast! \n The monster is a large, dinosaur type creature 🦖, with the ears of a goblin 👹, the eyes of an owl 🦉, the wings of a swan 🦢, and the spirit of a lion 🦁. \n What do you do?")

while True:
  option_1 = input("Do you want to befriend the monster 🤝 or do you want to attack the monster 💥 (Enter befriend or attack) ").lower()

  if option_1 == "befriend":
    print("The monster does not want to be your friend! He wants to fight! \n You lost 10 HP. It looks like you have to attack him")
    hp -= 10
    print("You now have {} HP " .format(hp))
    break

  elif option_1 == "attack" :
    print("Critical hit!")
    break

  else:
    print("This is an invalid option.")


print("The monster cowered away and dropped some items after you")

if weapon == 1:
print ("slice it with you mighty stick")
break

if weapon == 2
print ("launch a mighty bal of explosionynessy stuff at it")

print("You pick it up the things it dropped and now have 100 gold pieces and a bone!")
wallet = 100
inventory = 1
#in this case, 1 means bone to tame wolves