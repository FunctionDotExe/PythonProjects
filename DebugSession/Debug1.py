# DEBUG THE ENTIRE CODE

# PART 1: Print Statements
print("If you can't even debug the first line of code, you're in trouble!")

print("He looked up and yelled 'GET INTO THE CLASS SOON! YOU'LL MISS IT!'")

instructor = input("Who's your favourite instructor?")

print("You favourite instructor is {}".format(instructor))

# PART 2: Fix the Operations
name = input("What is your name?")

print("Hello {}!  Let's work out what you earned this week".format(name))

hourly_rate = int(input("How much do you earn per hour?"))

  

hours_worked = int(input("How many hours do you work per day? "))
if hours_worked < 24:


    days = int(input("How many days per week do you work? "))
    if days < 7:
      wages = hourly_rate * hours_worked * days
      print("Your pay this week before tax is: ${} ".format(wages))
      wages *= 0.80
      print("After tax @ 20% that is: ${}".format(wages))   
      
  
      
    else:
      print( "I think you did it wrong, cause their ain't more than 7 days in a week ")
     
else:
    print( "I think you did it wrong, cause their ain't more than 24 hours in a day")
   


# PART 3: If/Else Statements
score = 10
answer = input("Who is cooler, Thip or Mayu?")
answer = answer.strip().lower()

if answer == "thip":
  print("That is correct, you get 10 points!")
  score += 10
else:
  print("Sorry, that is incorrect, you lose 2 points")
  score -= 2

print("Your score is now: {} points".format(score))

answer2 = input("What is the name of Saturn's largest moon?")
answer2 = answer2.strip().lower()

if answer2 == "titan":
  print("That is correct, you get 10 points!")
  score += 10
elif answer2 == "ganymede":
  print("You're thinking of Jupiter! You lose 5 points")
  score -= 5
else:
  print("Sorry, incorrect, You lose 5 points")
  score -= 5
  
print("Your score is now: {} points".format(score))

# PART 4 Fix the Loops!
i = 0
while i < 10:
 
  print("This should print 10x!")
  i +=1

# Should count from 10 down to 1
i = 10
while i > 0:
  print(i)
  i -= 1
  

# Print out the numbers 1-12
for i in range(1,13):
  print(i)

NUMBER = 4
GUESSES = 5

for i in range(GUESSES):
  print("You have {} guesses left.".format(GUESSES - i))
  guess = int(input("Guess the number: "))
  
  if guess == NUMBER:
    print("Yes! That's right!")
    break
  else:
    print("Wrong!")
    
else:
  print("Out of guesses, the answer was {}!".format(NUMBER))
