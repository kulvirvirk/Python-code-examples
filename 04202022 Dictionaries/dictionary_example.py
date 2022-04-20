
# create a dictionary called Students, add student name as key and their GPA as a value

from turtle import setundobuffer


students = {"Nick": 4, "Tom": 3.2, "James":3.3, "Ram":4.0}
#print dictionary
print(students)

#access specific student's GPA by using the key
print(students["Nick"])

#add new item to the dictionary
students["Bob"] = 2.9
print(students)

#delete an item from the dictionary
del(students['Tom'])
print(students)
