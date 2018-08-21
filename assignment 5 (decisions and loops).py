# DECISION AND FLOW CONTROL

#Q.1- Take an input year from user and decide whether it is a leap year or not.
year=int(input())
if year%4==0:
    print("It is a leap year")
else:
    print('it is not a leap year')

#Q.2- Take length and breadth input from user and check whether the dimensions are of square or rectangle.
le=int(input())
br=int(input())
if le==br:
    print("SQUARE")
else:
    print('RECTANGLE')


#Q.3- Take the input age of 3 people and determine oldest and youngest among them.
ek=int(input())
do=int(input())
tin=int(input())
if ek>do:
    if ek>tin:
        print('ek is OLDEST. age = %d' % ek)
    else:
        print('tin is OLDEST. age = %d' % tin)
elif do>ek:
    if do>tin:
        print('do is OLDEST. age = %d' % do)
    else:
        print('tin is OLDEST. age = %d' % tin)
if ek<do:
    if ek<tin:
        print('ek is YOUNGEST. age = %d' % ek)
    else:
        print('tin is YOUNGEST. age = %d' % tin)
elif do<ek:
    if do<tin:
        print('do is YOUNGEST. age = %d' % do)
    else:
        print('tin is YOUNGEST. age = %d' % tin)
        
        
        

'''Q.4- Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service. 

1. if employee is female, then she will work only in urban areas. 
2. if employee is a male and age is in between 20 to 40 then he may work in anywhere 
3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only. 
4. And any other input of age should print "ERROR". '''
age=int(input('Enter age\n'))
sex=input('M or F\n')
mar=input('Y or N\n')
if sex=='F':
    print('Urban area')
elif age>20 and age<40:
    print('Anywhere')
elif age>40 and age<60:
    print('Urban area')
else:
    print('ERROR')




'''Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100.
Judge and print total cost for user.''' 
quan=int(input())
rate=100
amount=quan*rate
if amount>1000:
    amount=amount-(amount*0.10)
print(amount)

#LOOPS

#Q.1- Take 10 integers from user and print it on screen.
i=10
while i>0:
    x=int(input('input number\n'))
    print(x)
    i=i-1
#Q.2- Write an infinite loop.An infinite loop never ends. Condition is always true.
i=0
while True:
    i+=1
    print('n')
    if i==10:
        break
#we have created an infinite loop by while True but for the sake of other questions we need to break it so other programs can also run



#Q.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.
l=[]
n=int(input('enter length\n'))
l1=[]
for i in range(n):
    y=int(input())
    l.append(y)
    l1.append(y*y)
print(l)
print(l1)

#Q.4- From a list containing ints, strings and floats, make three lists to store them separately 
a=[1,'ab',3.14,0.65,54,43,'arsh']
intt=[]
fl=[]
st=[]
for j in a:
    if type(j)==int:
        intt.append(j)
    elif type(j)==float:
        fl.append(j)
    elif type(j)==str:
        st.append(j)
print(intt)
print(fl)
print(st)


#Q.5- Using range(1,101), make a list containing only prime numbers.
for num in range(1,101):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
    

    

'''Q.6- Print the following patterns: 
* 
** 
*** 
**** '''
j=1
while j<=4:
    print('*'*j)
    j=j+1
   
        

'''Q.7- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found.
Iterate over list using for loop. '''
lst=[]
num=int(input('enter the length of list\n'))
for v in range (num):
    c=input()
    lst.append(c)
find=input('to be searched\n')
for h in lst:
    if h==find:
        lst.remove(h)
print(lst)

