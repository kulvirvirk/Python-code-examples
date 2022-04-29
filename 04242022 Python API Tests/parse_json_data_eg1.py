import json

# Json object which has a key of 'people' and value of 'people' is array of more objects. 
# We have two objects here, and each object has a key called name, phone, email and emp_number.
# each key of object has further values paired with them. E.g. "name":"John"
people_string = '''
{
    "people":[
        {
            "name": "John", 
            "phone": "000 000 1234",
            "email": ["test123@gmail.com", "test456@gmail.com"], 
            "emp_number": 1 
        },
        {
            "name": "Kevin", 
            "phone": "123 123 1234",
            "email": ["test_Kevin@gmail.com", "test_Kevin6@gmail.com"], 
            "emp_number": 1 
        } 
    ]
}
'''

# load json into python object. loads() funciton
data = json.loads(people_string)  # json.loads() converts a json to python dictionary. 
for person in data['people']:
    print(person)
    #print(person["name"])      # prints the name of each person 
