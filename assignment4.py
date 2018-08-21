#Q.1- Reverse the whole list using list methods.
l1=[ 1, 2 , 'hey' ,4 , 5]
l1.reverse()
print(l1)


#Q.2- Print all the uppercase letters from a string.
b=input()
d=''
n=len(b)
for i in b:
    if i.isupper() == True:
        d=d+i
print(d)


#Q.3- Split the user input on comma's and store the values in a list as integers.
x=input()
q=x.split(',')

z=[]
for j in q:
    z.append(int(j))
print(z)
#l=list(map(int,input().split(',')))

#Q.4- Check whether a string is palindromic or not.
p=input()
s=p[::-1]
if p==s:
    print('PALINDROME')
else:
    print('NOT PALINDROME')


#Q.5- Make a deepcopy of a list and write the difference between shallow copy and deep copy.
import copy as c
li=[1,2,[3,4],5]
lj=c.deepcopy(li)
li[2][1]=6
li[1]=9
print(li)
print(lj)

'''the diiference between shallow copy and deepcopy is that
in shallow copy the duplicate reference variable points to the old object that is the nested mutable object is common between both
the lists and the change in the nested list will cause change in both the lists
whereas in deep copy the second list creates ts own different reference and no changes in the first lists either in other elements 
or nested elements cant affect the second list.
it is a totally differnt list un affected by the first one.
'''
