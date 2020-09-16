name = input('Enter name: ')
surname = input('Enter surname: ')
year = int(input('Enter year of birth: '))
city = input('Enter сity of residence: ')
email = input('Enter your email: ')
phone = input('Enter your phone number: ')

def show_info(*args):
	return f'\n{surname} {name} {year} {city} {email} {phone}'

print(show_info())