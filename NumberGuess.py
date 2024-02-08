import random

while True :
	try : 
		min_number=int(input("Enter a Minimum Number : "))
		max_number=int(input("Enter a Maximum Number : "))
		if max_number < min_number :
			print("Maximum number should be greater than minimum number")
			raise
		max_attempts=int(input("Enter number of attempts : "))
		if max_attempts <= 0 :
			print("Number of attempts should be greater than zero")
			raise			
		guess_number=int(input(f"Guess a number between {min_number} and {max_number} : "))
		if min_number > guess_number and max_number > guess_number :
			print(f"Number Guessed is out of range - {min_number} and {max_number}")
			raise	
		break
	except ValueError:
		print("\nEnter Valid input ")
	except Exception :
		print("\nEnter Valid input ")	

random_number=random.randint(min_number, max_number)	
num_iterations=1

while num_iterations < max_attempts :

	prev_guess_number=guess_number
	if min_number > guess_number and max_number > guess_number :
		print(f"Number Guessed is out of range - {min_number} and {max_number}")
	elif guess_number < random_number :
		print(f"Guessed Number {guess_number} is lesser than system generated number")
	elif guess_number > random_number :
		print(f"Guessed number {guess_number} is greater than system generated number")
	elif guess_number == random_number :
		print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")	
		print(f"!!! Wow! Congrats!! You won the game in {num_iterations} attempts !!!")
		print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")			
		break
	
	num_iterations = num_iterations + 1
	while True :
		try:
			guess_number=int(input(f"\nAttempt {num_iterations} - Guess number again : "))
			break
		except ValueError :
			print("Enter Valid input ")
			
if num_iterations == max_attempts :
	print("\n*******************************************************")
	print("*** All attempts are exhausted. Please try Again... ***")
	print("*******************************************************")
