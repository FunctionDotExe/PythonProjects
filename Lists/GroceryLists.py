groceryList = []
while True:
  
	itemAndNum = input("What do you want to add to the list and how much? ")

	print()
	print("Grocery List")
	groceryList.append(itemAndNum)
	list.sort(groceryList, reverse = True)
 
  


	tracker = 1
	for k in groceryList:
		print(str(tracker) + ". " + k)
		tracker += 1
	print()
	print()
