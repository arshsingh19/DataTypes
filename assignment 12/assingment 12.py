#Ques_1.print todays date


from datetime import date #importing datetime module
today=date.today()
print("Today's date is :-",today)#prting date




#Ques_2. playing a video in browser
import webbrowser
webbrowser.open_new('https://www.youtube.com/watch?v=_3b6LZ2xAVs&t=627s')#opening a youtube video in internet explorer



#Ques_3. changing the file extension in a directory
import os
Dir=os.listdir()
for i in range(1,len(Dir)):
    Dir[i],ext=os.path.splitext(Dir[i])
    os.rename(Dir[i]+'.txt',Dir[i]+'changed.jpg')
print(Dir)
