text = input('Enter string: ').split()

def int_func(text):
	join_text = ' '.join(text)
	return join_text.title()

print(int_func(text))