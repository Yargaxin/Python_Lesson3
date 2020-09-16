def div(n1, n2):
	try:
		return n1 / n2
	except:
		return 'Division by zero!'

print(div(int(input('Enter number: ')), int(input('Enter second number: '))))