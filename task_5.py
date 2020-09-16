numbers = input('Press Enter: ')
int_list = []
intermediate_list = []

print('Help!\ne = Exit,\nk = key word')
def sum_value(numbers):
	while True:
		numbers = input('\nEnter numbers or e or k: ').split()
		if numbers[0] == 'e':
			return 'Bye!'
			break
		elif numbers[-1] == 'k':
			del numbers[-1]
			for i in numbers:
				int_list.append(int(i))
			print(f'Sum: {sum(int_list)}')
			return 'Bye!'
			break
		else:
			for i in numbers:
				int_list.append(int(i))
			print(f'Sum: {sum(int_list)}')
		for i in numbers:
			intermediate_list.append(int(i))
		print(f'Intermediate sum: {sum(intermediate_list)}')
		intermediate_list.clear()

print(sum_value(numbers))