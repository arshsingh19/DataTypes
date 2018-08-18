#LISTS

#Q.1 - Create a list with user defined inputs.
l1=['info' , 'tcs' ,'wipro']
print(l1)


#Q.2- Add the following list to above created list: 
#[‘google’,’apple’,’facebook’,’microsoft’,’tesla’]
l1.append('google')
l1.append('apple')
l1.append('facebook')
l1.append('microsoft')
l1.append('tesla')
print(l1)

#Q.3 - Count the number of time an object occurs in a list.
n=l1.count('tesla')
print(n)

#Q.4 - create a list with numbers and sort it in ascending order.
l2=[4,6,3,6,3,5,1]
l2.sort()
print(l2)

#Q.5 - Given are two one-dimensional arrays A and B which are sorted in ascending order.
#Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order. [List]
A=[2,6,4,5,1]
A.sort()
B=[7,8,2,4]
B.sort()
c=[]
C=A+B
C.sort()
print(C)


#Q.6 - Count even and odd numbers in that list.
m=len(C)
e=0
o=0
for i in C:
    if i%2==0:
        e=e+1
    else:
        o=o+1
print("even = %d" % e)
print("odd = %d "  % o)
    
    

#TUPLES


#Q.1-Print a tuple in reverse order.
tup=('apple','banana','orange','mango')
tup2=reversed(tup)
print(tuple(tup2))




#Q.2-Find largest and smallest elements of a tuples.
tupl=(5,8,1,9,3)

print(max(tupl))
print(min(tupl))


#STRINGS


#Q.1- Convert a string to uppercase.
s=input()
s=s.upper()
print(s)

#Q.2- Print true if the string contains all numeric characters.
q=input()
print(q.isdigit())

#Q.3- Replace the word "World" with your name in the string "Hello World". 
str1="Hello World"
str1=str1.replace("World", "Arsh")
print(str1)
