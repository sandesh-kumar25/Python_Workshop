import random
r = random.randint(1,30)

while(True):
	inp = int(input())
	if(inp<r):
		print("Wrong guess,try a greater number")
	elif(inp>r):
		print("Wrong guess,try a smaller number")

	else:
		print("CONGRATULATIONS, you guessed the number")