#ASSIGNMENT - FUNCTIONS

#Q.1- Create a function to calculate the area of a sphere by taking radius from user.

r=int(input())
def areaSq(r):
    ar=4*3.14*r*r
    return ar

print(areaSq(r))

'''Q.2- Write a function “perfect()” that determines if parameter number is a perfect number.
Use this function in a program that determines and prints all the perfect numbers between 1 and 1000. 
[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number.
E.g., 6 is a perfect number because 6=1+2+3].'''
def perfect(num):
    j=0
    for i in range(1,num):
        if num%i==0:
            j=j+i
    if num==j:
        print(num)
for num in range (1,1000):
    perfect(num)
        
    

    



#Q.3- Print multiplication table of n using loops, where n is an integer and is taken as input from the user.
n=int(input())
def table(n):
    for i in range(1,11):
        print('{} * {} = {}'.format(n,i,n*i))
table(n)


#Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion.
a=int(input())
b=int(input())
def power(a,b):
    if b==1:
        return a
    else:
        return(a * power(a,b-1))
print(power(a,b))

#ASSIGNMENT - CLASSES AND OBJECTS

#Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.

'''Q.2- Create a Student class and initialize it with name and roll number. Make methods to : 
1. Display - It should display all informations of the student. 
2. setAge - It should assign age to student
3. setMarks - It should assign marks to the student.'''

'''Q.3- Create a Temprature class and create two methods: 
1. convertFahrenheit - It will take celsius and will print it into Fahrenheit. 
2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.'''

'''Q.4- Create a class MovieDetails and initialize it with artistname,Year of release and ratings . 
Make methods to 
1. Display-Display the details. 
2. Add- Add the movie details. '''

#Q.5- Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is inheriting Animal and access the base class method.

#Q.6- What will be the output of following code. IMAGE

#Q.7- Create a class Shape.Initialize it with length and breadth Create the method Area.
#Create class rectangle and square which inherits shape and access the method Area.
