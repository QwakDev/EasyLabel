#TODO videoSeparator
import cv2 as cv
import os
import numpy as np
import math
import matplotlib.pyplot as plt
def GetLabelsColors(path):
    labled_colors = []
    NAME_labels = []
    BGR_labels = None

    with open(path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                l = line.strip().split(',')
                ls = [l[0],int(l[1]),int(l[2]),int(l[3])]
                labled_colors.append(ls)
            BGR_labels = np.zeros((len(labled_colors),3))
    y = 0
    # ORGANIZE DATA np ARRAY of colors and list of LAbel NAMES
    for x in labled_colors:
        NAME_labels.append(x[0])
        BGR_labels[y,0] = x[1]
        BGR_labels[y,1] = x[2]
        BGR_labels[y,2] = x[3]
        y = y + 1
    BGR_labels = BGR_labels.astype(dtype=np.uint8)
    return BGR_labels, NAME_labels
def GetThresholdSize(shape, proc):
    (x,y, _) = shape
    out = (x * y) * (proc/100)
    return(int(out))
def GetRanges(color, dif):
    range1 = np.array([color[0], color[1], color[2]])
    range2 = np.array([color[0], color[1], color[2]])

    for i in range(3):
        reminder = 0
        if color[i] > dif & color[i] < (254 - dif):
            range1[i] = color[i] - dif
            range2[i] = color[i] + dif
        elif color[i] < dif:
            reminder = (color[i] - dif) * (-1)
            range1[i] = 0
            range2[i] = color[i] + dif + reminder
        elif color[i] > (254 - dif):
            reminder = (254 - color[i] - dif) * (-1)
            range1[i] = color[i] - dif - reminder
            range2[i] = 255 
    return range1, range2
#dif (looking for range in color +/-)
#
def SEPARATE(temp_dir_path, dif = 10):
    p_pic = temp_dir_path + '_temp.jpg' #ORGINAL PICTURE
    p_l_pic = temp_dir_path + 'temp.jpg' #LABLED PICTURE
    p_labels = temp_dir_path + 'Labels.txt' #SAVED LABELS WITH COLORS
    p_save = temp_dir_path

    #CREATE _Labels.txt (where labels for main folder will be stored)

    #READING LABEL FILE AND GETTING LABELS AND COLORS
    #['LABEL',b,g,r]
    BGR_labels, NAME_labels = GetLabelsColors(p_labels)
    #GETTING WORKING IMAGES
    img = cv.imread(p_pic) #ORGINAL
    lab_img = cv.imread(p_l_pic) #LABLED_IMAGE
    #threshold for contours
    th = GetThresholdSize(img.shape, 0.05)
    for i in range(len(NAME_labels)):
        color = BGR_labels[i]
        #MASK
        col1, col2 = GetRanges(color, 10)
        mask = cv.inRange(lab_img,col1,col2)
        #CONTOURS
        conts, h = cv.findContours(image=mask, mode=cv.RETR_TREE, method= cv.CHAIN_APPROX_NONE)
        con_img = np.zeros(mask.shape)
        cv.drawContours(image=con_img, contours=conts, contourIdx=-1, color=(255))


        file_number = 0
        for _,c in enumerate(conts):
            if cv.contourArea(c) > th:
                x,y,w,h = cv.boundingRect(c)
                toSave = img[y:y+h, x:x+w]
                _toSave = np.zeros(img.shape)
                cv.fillPoly(_toSave,pts = [c],color=(255,255,255))
                _toSave = _toSave[y:y+h, x:x+w]
                cv.imwrite(p_save + NAME_labels[i] + '_' + str(file_number) + '_.jpg', _toSave)
                cv.imwrite(p_save + NAME_labels[i] + '_' + str(file_number) + '.jpg', toSave)
                file_number = file_number + 1
            
