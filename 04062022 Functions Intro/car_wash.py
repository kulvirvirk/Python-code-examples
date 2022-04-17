

def regular_carwash():
    print("Spray water!!!")
    print("Put soap on.")
    print("Rinse")


def premium_carwash():
    print("=========Starting Premium Wash=========")
    print("Spray water!!!")
    print("Put soap on.")
    print("Rinse")
    print("Put soap on the second time.")
    print("Rinse again")
    print("Air dry!")
    print("========= Premium Wash Done =========")
print("Hello, please select your car wash (Regular or Premium): ")
user_selection = input()

if user_selection == "Regular":
    regular_carwash()

elif user_selection == "Premium":
    premium_carwash()

else:
    print("Invalid entry!")