'''Write a program: 
1. ask the user, "what's my fav food?" 
2. if its same as your fav food, print "amazing"
2. else print, "yuck"'''

print("Guess my favorite food:")
myFavFood = "Mexican"
usersInput = input("What's my fav food? ")
if (usersInput == myFavFood):
    print("Yep, so amazing!!")

else: print("Yuck! that's not it.")
print("Thanks for playing!")