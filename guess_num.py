import random as rn
def game() -> str:
	level = input('Enter level: ')
	while level != "Level doesn't exist" :
		if level == 'max' or level == 'MAX':
			n = rn.randint(1,100)
			break
		elif int(level)>=2 and int(level) <= 100:
			n = rn.randint(1,int(level))
			break
		else:
			print("Level doesn't exist")
		level = input('Enter level: ')
	gn = int(input(f'Guess a number [1-{level}] : '))
	if n == gn:
		return "yayyy !!! :)"
	return "oops :( "
p = 'y'
while p == 'y' or p == 'Y' :
	result = game()
	if result == 'yayyy !!! :)' :
		print(result)
		break
	print(result)
	p = input("Do you want to continue ? [y/N]")

