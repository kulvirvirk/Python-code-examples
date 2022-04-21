# from a give text count how many times each word appears. 

text = '''et qui proident voluptate excepteur enim Lorem ea id ipsum veniam
 culpa eu anim amet cupidatat ad ad culpa voluptate dolore esse et culpa pariatur
  consequat proident irure id voluptate officia nulla in aliqua est nisi 
  consectetur non aliqua duis nostrud Lorem et aliquip laborum qui do eu 
  commodo in aute qui nostrud elit sint aliqua quis eu in dolor magna aliqua
   consequat esse elit aute esse eu consequat consectetur enim deserunt esse 
   occaecat do ad est sit nostrud et ex est labore enim ad consequat 
adipisicing laboris est ex voluptate sunt velit enim aliqua ut minim officia ut ut'''

#convert the text into a list by using split()
text_to_list = text.split()

# use dictionary to hold the words as key and count as value. 

word_count = {}
for word in text_to_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)
print('--------------------------------')