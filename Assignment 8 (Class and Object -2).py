#Question 1
#Create a circle class and initialize it with radius.
#Make two methods getArea and getCircumference inside this class.

class Circle:
    def __init__(self,rad):
        self.rad=rad
    def Area(self):
        self.Area=3.14*(self.rad**2)
        return self.Area
    def Circum(self):
        self.Cir=2*3.14*self.rad
        return self.Cir
rad=int(input("Please Enter The Radius of the Circle"))
c1=Circle(rad)
print(c1.Area())
print(c1.Circum())


#Question 2
#Create a Student class and initialize it with name and roll number. Make methods to :
#1. Display - It should display all informations of the student.
#2. setAge - It should assign age to student
#3. setMarks - It should assign marks to the student.

class Student:
    def __init__(self,name,Rno):
        self.Name=name
        self.rno=Rno
    def setAge(self,age):
        self.Age=age
    def setMarks(self,marks):
        self.mark=marks
    def Display(self):
        print("Name: {}".format(self.Name))
        print("Roll No: {}".format(self.rno))
        print("Age: {}".format(self.Age))
        print("Marks: {}".format(self.mark))
name=input("Please Enter The Name of the Student ")
rollno=int(input("Please Enter The RollNo of the Student "))
age=int(input("Please Enter The Age of the Student "))
marks=int(input("Please Enter The Marks of the Student "))

S1=Student(name,rollno)
S1.setAge(age)
S1.setMarks(marks)
S1.Display()


# Question 3
# Create a Temprature class and create two methods:
# 1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
# 2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.

class Temp:
    def convertFahrenheit(self, Cel):
        self.Celc = Cel
        self.Farh = ((self.Celc * 9) / 5) + 32
        print("The Farh Conversion of {} is {}".format(self.Celc, self.Farh))

    def convertCelcius(self, Farh):
        self.Farh = Farh
        self.Cel = (self.Farh - 32) * 5 / 9
        print("The Celcius Conversion of {} is {}".format(self.Farh, self.Cel))


choice = ['1', '2']
T = Temp()
a = input("Input 1 for Converion to F and 2 for Conversion to C")
if a in choice:
    if a == '1':
        cel = int(input("Enter Temprature in Celcius"))
        T.convertFahrenheit(cel)
    else:
        far = int(input("Enter Temprature in Fahrenheit"))
        T.convertCelcius(far)
else:
    print("PLease Enter Valid Input")


#Question 4
#Create a class MovieDetails and initialize it with artistname,Year of release and ratings .
#Make methods to
#1. Display-Display the details.
#2. Add- Add the movie details.

class MovieDetails:
    Mov=list()
    def __init__(self,artName,YoR,Rat):
        self.Aname=artName
        self.RelYear=YoR
        self.ratings=Rat
    def Add(self):
        self.NewMov={'Artist':self.Aname,'Release Year':self.RelYear,'Ratings':self.ratings}
        self.Mov.append(self.NewMov)
    def Display(self):
        for i in range(0,len(self.Mov)):
            print("The Artist of the Movie is {}".format(self.Mov[i]['Artist']))
            print("The Year of Release is {}".format(self.Mov[i]['Release Year']))
            print("The Ratings are {}".format(self.Mov[i]['Ratings']))

DDLJ=MovieDetails('SRK','1998','5')
DDLJ.Add()
D3=MovieDetails('Aamir','2004','4')
D3.Add()
D3.Display()

#Upon Calling The Display Function The Output gives All the elements of the MOV list


# Question 5
# Create a class Animal as a base class and define method animal_attribute.
# Create another class Tiger which is inheriting Animal and access the base class method.

class Animal:
    def animal_attribute(self):
        self.Color = 'Yellow with Brown Stripes'
        self.legs = 4
        self.Endangered = 'Endangered'
        print(self.Color, self.legs, self.Endangered, sep="\n")


class Tiger(Animal):
    def Yellow(self):
        pass


Tig = Tiger()
Tig.animal_attribute()


#Question 6
#Find OUTPUT
#class A:
#    def f(self):
#        return self.g()

#    def g(self):
#        return 'A'

#class B(A):
#    def g(self):
#        return 'B'

#    a = A()
#    b = B()
#    print a.f(), b.f()
#    print a.g(), b.g()

#The Output of code Should be:-
# A A
# A B





#Question 7
#Create a class Shape.Initialize it with length and breadth Create the method Area.
#Create class rectangle and square which inherits shape and access the method Area.

class Shape:
    __length=0
    __brdth=0
    def GetMeas(self):
        self.__length=int(input("Enter The Length Of the Shape "))
        self.__brdth=int(input("Enter The Breadth of the Shape "))
        return self.__length,self.__brdth
    def Area(self,leng,brd):
        self.Ar=leng*brd
        print(self.Ar)
class Rectangle(Shape):
    def __init__(self):
        pass
class Square(Shape):
    def __init__(self):
        pass

Sq=Square()
Rc=Rectangle()
sh=Shape()

ln,brd=sh.GetMeas()
if ln==brd:
    Sq.Area(ln,brd)
else:
    Rc.Area(ln,brd)
