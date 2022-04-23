# create a program that lets the user guess the random number picked by the code. 
# each loop it lets user try the number and tell them to go higher or lower.

# fuction to generate the random number
import random

def generate_random_num():
    return random.randint(1, 100)

# get user's name
user_name = input("Enter you name to begin the :")
print(f"Hello {user_name}, let's play... \n\n`````````Random Number Guessing Game`````````\n")

# get a random number from generate_random_num() function.
random_number = generate_random_num()

# get uers's input
user_num_entry = int(input("I have generated a random number between 1 - 100, take a guess:"))

while user_num_entry != random_number:
    user_num_entry = int(input("Nope, try another number:"))
print ("You got it!")