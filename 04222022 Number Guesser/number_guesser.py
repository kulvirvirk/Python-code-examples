# create a program that lets the user guess the random number picked by the code. 
# each loop it lets user try the number and tell them to go higher or lower.


import random
random_number = random.randint(1, 100)

user_name = input("Enter you name to begin the :")
print(f"Hello {user_name}, let's play... \n\n`````````Random Number Guessing Game`````````\n")