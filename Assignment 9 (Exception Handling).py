#ASSIGNMENT- EXCEPTION HANDLING

#Q.1- Name and handle the exception occured in the following program: 

    
a=3
if a<4:
    try:
        a=a/(a-3)
    except ZeroDivisionError as msg:    
        print(msg) 
#zero divison error handled
   

#Q.2 - Name and handle the exception occurred in the following program: 


#IndexError because the index in print command is out of the list

l=[1,2,3]
try:
    print(l[3])
except IndexError as ms:
    print(ms)
    
    


'''#Q.3- What will be the output of the following code:

    # Program to depict Raising Exception
     
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print("An exception")
    raise  # To determine whether the exception was raised or not'''
#The output of the above code will simply line printed as “An exception” but a Runtime error will also occur in the last due to raise statement in the last line.


'''Q.4- What will be the output of the following code: 

     # Function which returns a/b
    def AbyB(a , b):
        try:
            c = ((a+b) / (a-b))
        except ZeroDivisionError:
            print("a/b result in 0")
        else:
            print(c)
    
    # Driver program to test above function
    AbyB(2.0, 3.0)
    AbyB(3.0, 3.0)'''
#output of the following code will be
# -5.0    (returns float value as it goes to else)
# a/b result in 0       (error occurs because of zreo division so goes to except)
    
'''Q.5- Write a program to show and handle following exceptions: 
1. Import Error 
2. Value Error 
3. Index Error '''

#ImportError
try:
    from .yayeet import*
except ImportError as ya:
    print(ya)

#ValueError
try:
    q=int(input())
except ValueError as d:
    print(d)
else:
    print(q)
    
#IndexError and ValueError combined
l=[11,22,33]
try:
    i=int(input())
    print(l[i])
except IndexError as ms:
    print(ms)
except ValueError as ms:
    print(ms)
