# create a program that lets the user guess the random number picked by the code. 
# each loop it lets user try the number and tell them to go higher or lower.

# fuction to generate the random number
import random
import time

def generate_random_num():
    return random.randint(1, 100)

# get user's name
user_name = input("Enter you name to begin:")
print(f"Hello {user_name}, let's play... \n\n`````````Random Number Guessing Game`````````\n")

print("Generating a random number...\n")
time.sleep(3)
random_number = generate_random_num()   # get a random number from generate_random_num() function.
guess_counter = 1

# get uers's input
user_num_entry = int(input("I have generated a random number between 1 - 100, take a guess:"))

while user_num_entry != random_number:
    if(user_num_entry < random_number):
        print("Go higher.")
    elif (user_num_entry > random_number):
        print("Go lower.")
    user_num_entry = int(input("Try another number:"))
    guess_counter = guess_counter + 1

print (f"Congratulation! You got it {user_name}, it took you {guess_counter} tries.\n")