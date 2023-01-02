1#importing the time module
import time 

#welcoming the user 
name = input("what is the name of the you? ")

print ("Hello " + name + ". Let's play hangman!")

#wait for 1 second
time.sleep(1)

print ("Start guessing...( It's 7 letters)")
time.sleep(0.5)

#here we set the word 
word = "pecking"

#creates an variable with an empty value
guesses = ""

#determine the number of chances 
turns = 8

# Create a while loop

#check if the turns are more than zero
while turns > 0: 

   # make a counter named failed that starts with zero
  failed = (0)

  # for every character in secret_word
  for char in word:
     
    # see if the character is in the players guess
    if char in guesses:
   
      # print then out the character
      print (char)

    else:
      
     # if not found, print a dash
      print("_")

    # and increase the failed counter with one
    failed += 1