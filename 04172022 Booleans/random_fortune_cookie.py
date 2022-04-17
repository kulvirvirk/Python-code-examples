# use a random number generator to provide the random number to user

import random

random_lucky_number = random.randint(1,10)
random_fortune_msg = random.randint(1,3)


print(f"Have a good day. \nYour lucky number is:{random_lucky_number}")

if random_fortune_msg == 1:
    print("You'll win lotto today!")
if random_fortune_msg == 2:
    print("You'll get married this year!")
if random_fortune_msg == 3:
    print("You'll get a promotion this year!")

