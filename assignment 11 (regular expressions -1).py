
#ASSIGNMENT- REGULAR EXPRESSIONS IN PYTHON

#Q.1- Write a python code to find a valid email address from a text.
import re
em=input("enter email address\n")
matcher = re.finditer('^\w[_a-zA-Z0-9.]*(@)(gmail.com|yahoo.com)$',em)

count=0
for m in matcher:
    count += 1
    #print('Match is at:{}, End:{}, Pattern found: {}'.format(m.start(), m.end(), m.group()))
if count>0:
    print('{} is a Valid email address'.format(em))
else:
    print('{} is NOT a Valid email address'.format(em))



#Q.2- Write a python program to find a valid Indian phone number from a text.
#(Valid Indian numbers will start with "+91-" and after that [6-9] followed by 9 digits. )
import re
mno=input("enter mobile no\n")
matcher = re.finditer('^[+]91[-][6-9][0-9]{9}$',mno)

count=0
for m in matcher:
    count += 1
    #print('Match is at:{}, End:{}, Pattern found: {}'.format(m.start(), m.end(), m.group()))
if count>0:
    print('{} is a Valid INDIAN number'.format(mno))
else:
    print('{} is NOT a Valid INDIAN number'.format(mno))
