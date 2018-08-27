#ASSIGNMENT - CLASSES AND OBJECTS

#Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.
'''class circle:
    def __init__(self,r):
        self.radius=r

    def getArea(self):
        print(3.14*self.radius*self.radius)

    def getCircumference(self):
        print(2*3.14*self.radius)
radius=int(input("enter radius\n"))
C=circle(radius)
C.getArea()
C.getCircumference()'''


'''Q.2- Create a Student class and initialize it with name and roll number. Make methods to : 
1. Display - It should display all informations of the student. 
2. setAge - It should assign age to student
3. setMarks - It should assign marks to the student.'''
'''class Student:
    def __init__(self,name,rno):
        self.name=name
        self.rno=rno
    def display(self):
        print('Name - {}'.format(self.name))
        print('Roll no - {}'.format(self.rno))
        print('Age - {}'.format(self.age))
        print('Marks - {}'.format(self.marks))
    def setAge(self,a):
        self.age=a

    def setMarks(self,m):
        self.marks=m

S=Student('arsh',1177)
S.setAge(20)
S.setMarks(95)
S.display()'''


'''Q.3- Create a Temprature class and create two methods: 
1. convertFahrenheit - It will take celsius and will print it into Fahrenheit. 
2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.'''



'''Q.4- Create a class MovieDetails and initialize it with artistname,Year of release and ratings . 
Make methods to 
1. Display-Display the details. 
2. Add- Add the movie details. '''

#Q.5- Create a class Animal as a base class and define method animal_attribute.
#Create another class Tiger which is inheriting Animal and access the base class method.

'''Q.6- What will be the output of following code. 

   ''' class A:
        def f(self):
            return self.g()

        def g(self):
            return 'A'

    class B(A):
        def g(self):
            return 'B'

    a = A()
    b = B()
    print (a.f(), b.f())
    print (a.g(), b.g())'''

    
#Q.7- Create a class Shape.Initialize it with length and breadth Create the method Area.
#Create class rectangle and square which inherits shape and access the method Area.
