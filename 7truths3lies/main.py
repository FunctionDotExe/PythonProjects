class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
facts = open('answer.txt','r')
answers = facts.readlines()
facts = {}

for i in answers:
  if "True" in i:
    i = i.replace("-True","")
    i = i.replace("\n","")
    facts[i] = True
  elif "False" in i:
    i = i.replace("-False","")
    i = i.replace("\n","")
    facts[i]= False
    
# this is where we show the screen thingy
print(bcolors.OKGREEN + "Welcome to 7 truths 3 lies :D!" + bcolors.ENDC)
print(bcolors.OKBLUE + "In this game there wil be 7 truths and 3 lies" + bcolors.ENDC)
print(bcolors.WARNING + "your task is to find all the lies" + bcolors.ENDC)
print(bcolors.OKGREEN + "if u fail to find all the lies then you have to go study brain anatomy" + bcolors.ENDC)
print(bcolors.FAIL + "have fun :P" + bcolors.ENDC)
print()

won = False
truth = 7
lie = 3
#while u havent won yet
while(not won):
  print(bcolors.FAIL + "Facts" + bcolors.ENDC)
  num = 1
  for j in facts :
    print(str(num)+ ". " + j)
    num += 1
  print()
  player = int(input(bcolors.OKBLUE + "Guess which number u think is a lie" + bcolors.ENDC)) - 1
  # if they guess a truth as a lie tell it to say that plater was wrong
  if(facts[list(facts)[player]]):
    truth -=1
    print(bcolors.OKBLUE+"That was a truth!:P " + str(truth) +" Truths left and " + str(lie) + " lies left :D"+bcolors.ENDC)
    facts.pop(list(facts)[player])

 ## checking how many lies are left and saying if u got a lie
  else:
	  lie -= 1
	  print(bcolors.WARNING + "NICE! That was a lie! " + str(truth) +" Truths left and " + str(lie) + " lies left!"+bcolors.ENDC)
	  facts.pop(list(facts)[player])
 # if u got all the lies
  if(lie == 0):
    print(bcolors.OKGREEN + "Nice ya got all the lies :D"+bcolors.ENDC)
    won = True
 #if u didnt get all the lies
  if(lie > truth):
    print(bcolors.WARNING     +"you missed some of the lies :P"+bcolors.ENDC)
    won = True
  print()
  




 