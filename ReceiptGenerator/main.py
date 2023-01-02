#Here is some simple Python code to generate a receipt

#Variable Declarations:
receipt = ""
total = 0
ask = "Y"


# The keyword "while" here indicates a loop. All the code that is indented following the "while" will be repeatedly executed until the expression in brackets (ask == "Y") is no longer true. This expression is checking if the value in the "ask" variable is "Y", if so, the indented block will run again.

while (ask == "Y"):
  #"print()" prints instruction to the console for the user to read.

  print("Enter name of item:")

  #"input()" prompts the user to type in the conosle, and we store that input in this variable.

  name = input()

  print("Enter price of item:")
  price = input()
  total = total + float(price)

  #The pink highlighted "\n" in the string changes the format of the string. It's like the ENTER key, it tells the string to stop writing on this line and begin again on the next.
  
  receipt = receipt + name + "...................."+price+"\n"

  print("Do you have more items to enter? (Y/N)")
  ask = input()

tax = total * 0.13
print("--------------RECEIPT--------------")
print(receipt)
print("TAX..............................",tax,"\n")
print("________________________________________")
print("TOTAL:                            ", total + tax);

"""
Translate the comments to C# too! Remember the comment syntax is 
different.
"""




