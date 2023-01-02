#making the function
def math(number):
  total = 0
  #while loop to do stuff while it is  true
  while True:
    total = number + total
    number -= 1
    #if the number is not = to 0  
    if number != 0:
      continue
    else: 
      break
  return total
  #text output
number = int(input("Your Number is : "))
print(math(number))
again = (input("would ya like todo again?"))
if again  == "yes" : 
    numberAgain = int(input("Your Number is : "))
    print(math(numberAgain))  