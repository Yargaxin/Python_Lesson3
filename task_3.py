n1 = int(input('Enter number: '))
n2 = int(input('Enter second number: '))
n3 = int(input('Enter third number: '))

def my_func(n1, n2, n3):
	list_n = [n1, n2, n3]
	sorted_list = sorted(list_n)
	zero_index = sorted_list[0]
	sorted_list.remove(zero_index)
	
	return sum(sorted_list)

print(my_func(n1,n2,n3))