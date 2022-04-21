

# From given piece of text: 
# count the number of chars. 

text = '''et qui proident voluptate excepteur enim Lorem ea id ipsum veniam
 culpa eu anim amet cupidatat ad ad culpa voluptate dolore esse et culpa pariatur
  consequat proident irure id voluptate officia nulla in aliqua est nisi 
  consectetur non aliqua duis nostrud Lorem et aliquip laborum qui do eu 
  commodo in aute qui nostrud elit sint aliqua quis eu in dolor magna aliqua
   consequat esse elit aute esse eu consequat consectetur enim deserunt esse 
   occaecat do ad est sit nostrud et ex est labore enim ad consequat 
adipisicing laboris est ex voluptate sunt velit enim aliqua ut minim officia ut ut'''

# count number of chars
print("Number of chars in this text: ")
print(len(text))
print('--------------------------------')

# count the number of words in the list
print("Number of words in this text: ")

# The split() method splits a string into a list. 
# you can call split() on text and then use len() to figure out the length of the list that you get back
print(len(text.split()))
print('--------------------------------')