#Question1
#Write a Python program to read n lines of a file

f=open("a.txt")
lines=[]
n=int(input("Enter The Number of lines you want to read "))
for i in range(0,n):
    line=f.readline()
    print(line)


# Question 2
# Write a Python program to count the frequency of words in a file.
f=open('a.txt')
lines=f.readlines()
wors=[]
count=[]
for l in lines:
    words=l.split()
    wors=wors+words
Wrd=set(wors)
for i in Wrd:
    cnt=0
    for j in wors:
        if i==j:
            cnt=cnt+1
    count.append(cnt)
wrds=list(Wrd)
for i in range(0,len(wrds)):
    print("The Count of {} is :{}".format(wrds[i],count[i]))



# Question 3
# Write a Python program to copy the contents of a file to another file
f=open('a.txt')
F=open('ac.txt','w')
f_data=f.read()
F.write(f_data)
f.close()
F.close()




# Question 4
# Write a Python program to combine each line from first file with the corresponding line in second file.
f = open('a.txt', 'r+')
F = open('a1.txt', 'r+')
g = open('a2.txt', 'w')
lines = f.readlines()
lines1 = F.readlines()
lines2 = list()
#print(lines)
#print(lines1)
if len(lines) > len(lines1):
    for i in range(0, len(lines1)):
        lines2.append(lines[i] + lines1[i])
    for i in range(len(lines1), len(lines)):
        lines2.append(lines[i])
else:
    for i in range(0, len(lines)):
        lines2.append(lines[i] + lines1[i])
    for i in range(len(lines), len(lines1)):
        lines2.append(lines1[i])
for i in range(0, len(lines2)):
    lines2[i] = lines2[i].replace('\n', ' ')
    g.writelines(lines2[i] + '\n')

f.close()
F.close()
g.close()




#Question 5
#Write a Python program to write 10 random numbers into a file.
#Read the file and then sort the numbers and then store it to another file.

f=open('a3.txt')
g=open('a4.txt','w')
lines=f.readlines()
#print(lines)
for i in range(0,len(lines)):
    lines[i]=int(lines[i])
lines=sorted(lines)
for i in range(0,len(lines)):
    lines[i]=str(lines[i])
    g.writelines(lines[i]+'\n')
f.close()
g.close()
