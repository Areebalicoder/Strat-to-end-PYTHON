# Using aray to make data
# Aray `[]` are used to store multipal data like

a=[1,2,5,7,"Python",21,"is easy language"]
print(a)

# we use this to stare like data in one variable like

myinfo=["Areebali","Shivji", 15,"years old","knows python very well", "born on",31,"May",2007]
print("")
print(myinfo)
print("")

# Now i can take any value form my data like i want my name so I can do this
print(myinfo[0],myinfo[1])
print("")

# Aray numbering is like this 
# ["Areebali","Shivji", 15,"years old","knows python very well", "born on",31,"May",2007]
# [     0    ,  1     , 2 ,      3    ,  4                      , 5       , 6, 7,   8  ]
# basically it starts from 0 and then goes on till the end of the data

print(len(myinfo)) # we use this to see total number of data stored in the arrya and the value of of len will be always be greater or 1 more than the numbering of data stored in the arrya

# making a program using the arry 







# Using cv2 program
# Cv2 is used for accssing camera
# This code programed for take a photo

import cv2

vid = cv2.VideoCapture(0) # VideoCapture() is function that helps to activate camera frame  

while True:              # While is a conditional function

    ret, frame = vid.read()  #.read() is used for reading the data

    cv2.imshow('Controlling my computer camera', frame)         #iamshow() is mainly used for showing some command and variable in the process of photo taking

    if cv2.waitKey(4) & 0xFF == ord('q'):     # .waitkey() is used for making a specfic key working for a command
        break


vid.release()   # making vid value 0 by release
cv2.destroyAllWindows()  # destroy all windows to prevent memory leaks







