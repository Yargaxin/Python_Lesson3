x = int(input('Enter positive number: '))
y = int(input('Enter negative number: '))

def exponentiation(x, y):
	c = x ** y
	return round(c, 3)

print(exponentiation(x,y))