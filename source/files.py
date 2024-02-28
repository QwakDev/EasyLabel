import tkinter as tk
import os
import cv2 as cv
from PIL import Image
import os
import io
#TODO LABEL.txt, config.txt, 1.jpg, 2.jpg... 
def GetNumberOfPictures(path):
    return len(GetListOfFiles(path)) - 1
def CreateConfigFile():
    return 0
def AppendLabelFile(path, label):
    (labels, _) = GetLabels(path)
    toSave = ','.join(map(str,labels))
    if toSave == '':
        toSave = str(label)
    else:
        toSave = toSave + ',' + str(label)
    f = open(path + 'Label.txt', 'w')
    f.write(toSave)

    return 0
def GetLabels(path): # RETURNS: (LIST_OF_LABELS,LIST_OF_ALL_LABELS)
    out = [[],[]]
    f = open(path + 'Label.txt', 'r')
    out[0] = f.read().split(',')
    out[1] = list(set(out[0])) #GETING LIST OF UNIQUE VALUES
    return out
def GetListOfFiles(path): #TODO Make sure they are files, FUTURE filtering
    out = []
    if os.path.isdir(path):
        _listOfFiles = os.listdir(path)
        for i in _listOfFiles:
            out.append(i)
    else:
        out = False
    return out
def GetPicture(path):#TODO read img and return it IN THE FUTURE transform
    return Image.open(path)
def SetSavingDir(path):#TODO  OR Output of wrong path given
    if os.path.isdir(path):
        if os.path.exists(path + 'Label.txt'):
            return GetNumberOfPictures(path)
        os.open(path + 'Label.txt', os.O_CREAT)
        return GetNumberOfPictures(path)
    else:#CREATING NEW DIR
        os.mkdir(path)
        os.open(path + 'Label.txt', os.O_CREAT)
        return 0
    
def SaveFile(path, data, label):
    name = GetNumberOfPictures(path)
    data.save(path + str(name) + '.jpg')
    AppendLabelFile(path, label)

    return 0

