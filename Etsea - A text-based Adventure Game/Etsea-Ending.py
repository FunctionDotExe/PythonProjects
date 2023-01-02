class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '1tt\033[1m'
    UNDERLINE = '\033[4m'
  #https://fsymbols.com/text-art/
  # You vs the game
def RubenEnd(): 
  #talkie part
  choice_Ruben1 = input(bcolors.FAIL + " You shouldnt be here \n we might have brought you here to adventure, but you have reached too far \n (type a to continue)" + bcolors.ENDC)
  if choice_Ruben1 == "a" :
    print(bcolors.OKGREEN + " What do you mean - Player(youself)" + bcolors.ENDC)
    choice_Ruben2 = input(bcolors.FAIL + " NOBODY FORCED YOU TO BE HERE, YOU DID YOURSELF! \n IT IS TIME FOR YOU TO END YOUR ADVENTURE" + bcolors.ENDC)
    if choice_Ruben2 == "a" :
      print(bcolors.OKGREEN + " i choose what i want to do, this is a choice game afterall "+ bcolors.ENDC)
    
    choice_Ruben3 = input(bcolors.FAIL + "  Now choose, either u die, or I kick you from the game.(Fight or leave)" + bcolors.ENDC)
    # leave choice
    if choice_Ruben3 == "leave" :
        print(bcolors.FAIL + " Very well then, You chose the good option" + bcolors.ENDC)
   #fight choice
    if choice_Ruben3 == "fight" :
      choice_Ruben4 = input(bcolors.OKGREEN + "I WILL FIGHT TO THE END" + bcolors.ENDC) 
      if choice_Ruben4 == "a" :
          print(bcolors.FAIL + " Very well then. I WILL SEE YOU IN HELL" + bcolors.ENDC)
          print("""__¶_____________________________________________¶
__¶¶___________________________________________¶¶
__¶¶¶¶________________________________________¶¶¶
__¶¶_¶¶_____________________________________¶¶_¶¶
__¶¶__¶¶___________________________________¶¶__¶¶
__¶¶_¶_¶¶_________________________________¶¶_¶_¶¶
__¶¶__¶__¶_______________________________¶¶_¶__¶¶
__¶¶___¶__¶¶____________________________¶__¶___¶¶
___¶¶___¶¶_¶¶_________________________¶¶__¶___¶¶
____¶¶___¶¶_¶¶_______________________¶¶_¶¶___¶¶¶
_____¶¶___¶¶__¶_____________________¶¶_¶¶____¶¶
______¶¶___¶¶__¶¶__________________¶__¶¶___¶¶¶
_______¶¶____¶¶_¶¶_______________¶¶_¶¶¶____¶¶
________¶¶____¶¶_¶¶_____________¶¶_¶¶____¶¶¶
_________¶¶____¶¶__¶¶__________¶__¶¶____¶¶¶
__________¶¶_____¶¶_¶¶_______¶¶__¶¶____¶¶
___________¶¶_____¶¶_¶¶_____¶¶_¶¶_____¶¶
_____________¶¶____¶¶__¶¶__¶__¶¶____¶¶¶
______________¶¶¶____¶¶_¶¶¶_¶¶¶___¶¶¶
________________¶¶¶___¶¶__¶¶¶___¶¶¶¶
__________________¶¶¶___¶¶_¶¶__¶¶¶
____________________¶¶¶__¶¶_¶¶¶¶
____________________¶_¶¶¶__¶¶_¶¶___¶¶¶¶¶¶
_________¶¶¶¶¶¶¶¶_¶¶_¶¶_¶¶__¶¶_¶¶¶¶¶¶¶¶_¶¶
________¶¶_¶¶¶¶¶¶¶¶_¶¶_¶¶¶¶¶__¶¶¶¶¶¶__¶¶_¶¶
________¶¶¶¶___¶¶¶¶¶__¶¶___¶¶¶¶¶¶¶¶¶¶__¶¶¶¶
_____________¶¶¶¶¶¶¶¶¶_______¶¶¶¶¶_¶¶¶
___________¶¶¶_¶_¶¶¶¶¶______¶¶¶_¶¶¶_¶¶¶¶
__________¶¶¶_¶_¶¶__¶¶¶_____¶¶¶__¶¶¶__¶¶¶
_________¶¶_¶¶_¶¶__¶¶_¶_____¶_¶¶__¶¶_¶_¶¶¶
_______¶¶¶_¶_¶¶¶__¶¶_¶¶_____¶¶_¶___¶¶_¶¶_¶¶¶
______¶¶_¶¶_¶¶¶____¶¶¶_______¶¶¶_____¶¶_¶_¶¶¶¶
_¶¶¶¶¶¶_¶_¶¶¶_________________________¶¶_¶¶_¶¶¶¶¶¶
¶¶____¶¶_¶¶¶____________________________¶¶_¶¶____¶
¶¶_____¶¶¶¶______________________________¶¶_____¶¶
_¶¶¶____¶¶_______________________________¶____¶¶¶
__¶¶¶¶__¶¶_______________________________¶¶¶¶¶¶¶
____¶¶¶¶¶_________________________________¶¶¶
""")
  choice_Ruben5 = input(bcolors.OKBLUE + "You are versing the game, this will be tough \n he has spawned himself into 'gltich' the worse mob never discovered \n you can do it \n Glitch spawns in the infinity sword, the most OP weapon in the game! \n You find a stick, what are you going to do with it? (Attack, Keep weapon)" + bcolors.ENDC) 
  if choice_Ruben5 == "Keep" :
    print(bcolors.FAIL + " he still can kill you, i dont know if u know that" + bcolors.ENDC)
  if choice_Ruben5 == "attack" :
    print(bcolors.OKBLUE + "You used the stick and yeet it right at glitch, CRITICAL HIT!" + bcolors.ENDC)

    choice_Ruben6 = input(bcolors.OKBLUE + " Glitch trys to hit you! You should dodge it! (dodge, stay still)"+ bcolors.ENDC) 
    if choice_Ruben6 == "Stay still" :
      print(bcolors.FAIL + " Bruh" + bcolors.ENDC)
    if choice_Ruben6 == "dodge" :
      print(bcolors.FAIL + "Nice! You rolled left and made glitch miss his swing" + bcolors.ENDC)
    choice_Ruben7 = input(bcolors.OKGREEN + " Wait wut is that? (look around or continue)"+ bcolors.ENDC) 
    if choice_Ruben7 == "continue" :
            print(bcolors.FAIL + "while u were thinking glitch took another swing and didnt miss! Good on him,for you, uhhh lets just not answer that" + bcolors.ENDC)
    if choice_Ruben7 == "look around" :
            print(bcolors.OKBLUE + " you start to look around and see a handle sticking out of the ground, you pull it out, it takes a few seconds and you got .... THE END SWORD\n this weapon was made for the builders of this game \n who sadly died from glitch, this is the only thing to kill him!" + bcolors.ENDC)
            print(bcolors.OKGREEN + """
-----------//¤¤\\
----------// ¤¤ \\
----------\\ ¤¤ //
---------- \\¤¤//
---------- (____)
-----------(____)
-----------(____)
-----------(____)
-\_____/\__/-----\__/\____/
--\_°_[-------------] _°_/
------\_°_¤ ---- ¤_°_/
-----------\ _°_ /
-----------|\_°_/|
-----------[|\_/|]
-----------[|[¤]|]
-----------[|;¤;|]
-----------[;;¤;;]
----------;;;;¤]|]\
---------;;;;;¤]|]-\
--------;;;;;[¤]|]--\
-------;;;;;|[¤]|]---\
------;;;;;[|[¤]|]|---|
-----;;;;;[|[¤]|]|---|
------;;;;[|[¤]|/---/
-------;;;[|[¤]/---/
--------;;[|[¤/---/
---------;[|[/---/
----------[|/---/
-----------/---/
----------/---/|]
---------/---/]|];
--------/---/¤]|];;
-------|---|[¤]|];;;
-------|---|[¤]|];;;
--------\--|[¤]|];;
---------\-|[¤]|];
-----------\|[¤]|]
------------\\¤//
-------------\|/
--------------V""" + bcolors.ENDC)


RubenEnd()