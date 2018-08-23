#ASSIGNMENT- DICTIONARIES

#Q.1- Create a user defined dictionary and get keys corresponding to the value using for loop.

mydict = {'george' : 16, 'arsh' : 17, 'amber' : 17}
search_age = int(input("Provide age\n"))
for name, age in mydict.items():
    if age == search_age:
        print(name)
    


'''Q.2- Create a dictionary and store student names and create nested dictionary to store the subject wise marks of every student.
Print the marks of a given student from that dictionary for every subject. 
Hint: Use nested dictionary to store subjects marks.'''
