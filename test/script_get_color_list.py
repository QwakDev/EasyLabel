import os
import random
# copy values from : https://www.tcl.tk/man/tcl8.6/TkCmd/colors.htm list and paste it to <<FILE.txt>>
#print(os.path.exists(<<FILE.txt>>))

file = open(<<FILE.txt>>)
Lines = file.readlines()
c = 0
colList = []
linesList = []

for line in Lines:
    linesList.append(line)
    c +=1
    if c % 8 == 0:
        col = linesList[0].rstrip()
        red = linesList[2].rstrip()
        green = linesList[4].rstrip()
        blue = linesList[6].rstrip()
        #print('COLOR: {}: R:{}, G:{}, B:{}'. format(col, red, green, blue))
        c = 0
        colList.append((col,blue,green,red))
        linesList = []
    #print('Line{}: &{}&'.format(c,line.rstrip()))

random.shuffle(colList)
with open(<<New.txt>>, 'w') as f:
        f.write('ColorName,BLUE,GREEN,RED)\n')
for x in colList:
    (c, b, g, r) = x
    with open(<<New.txt>>, 'a') as f:
        f.write("('{}',{},{},{}),\n".format(c,b,g,r))


