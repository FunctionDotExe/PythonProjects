
#using a def 
def generator(genI):
#using for loop to loop   3 times or the power to 3
	for i in genI:
		yield i * i * i
# numbers that it should multiply by
product = generator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#prinitng the sum of numbers
print(next(product))

print(next(product))

print(next(product))

print(next(product))

print(next(product))

print(next(product))

print(next(product))

print(next(product))

print(next(product))

print(next(product))
