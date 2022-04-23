
# create a function and when calling the function pass the argument value.

def say_hello(name):
    print(f"Hello {name}!")
say_hello("Nick")
print('--------------------------------')

# use for loop to say hello 5 times and pass the parameter "John"
for number in range(5):
    say_hello("John")
print('--------------------------------')

# create add_nums function and pass two numbers as arguments. 
def add_nums (num1, num2): 
    print(f"Sum of {num1} and {num2} = {num1 + num2}")

add_nums(5, 2)

print('--------------------------------')


# now create a function that returns a string but all uppercase 

def convert_string_to_uppercase(some_text):
    return some_text.upper()

uppercase_string = convert_string_to_uppercase("Test String")
print(f"Converted string: {uppercase_string}")

for number in range(5):
    print(f"Converted string: {uppercase_string}")