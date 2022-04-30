# declare variable and use is later in fuction
'''
age = 22
name = "John Doe"

print("User name is: " + name + " the age is: " + str(age))
'''
userName = input("Hello, what is your name? ")
print("Nice to meet you " + userName + "!")

user_response = input("Do you like learning python?(Yes/No) ")
if user_response == "Yes" or user_response == "yes":
    print("Awesome! keep going.")
else: 
    print("O no, that makes me sad :(")