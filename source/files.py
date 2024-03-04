import tkinter as tk
import os
import cv2 as cv
from PIL import Image , ImageTk
import os
import io
#TODO LABEL.txt, config.txt, 1.jpg, 2.jpg... 
def GetNumberOfPictures(path):
    return len(GetListOfFiles(path)) - 2
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
def GetListOfFiles(path):
    out = []
    if os.path.isdir(path):
        _listOfFiles = os.listdir(path)
        for i in _listOfFiles:
            out.append(i)
    else:
        out = False
    return out
def GetPicture(path):
    return ImageTk.PhotoImage(file=path)
def SetSavingDir(path):
    SetTempDir(path)
    if os.path.isdir(path):
        if os.path.exists(path + 'Label.txt'):
            return GetNumberOfPictures(path)
        os.open(path + 'Label.txt', os.O_CREAT)
        return GetNumberOfPictures(path)
    else:#CREATING NEW DIR
        os.mkdir(path)
        os.open(path + 'Label.txt', os.O_CREAT)
        return 0
    
def SaveFile(path, data, label, toTemp=False):
    name = ''
    if toTemp:
        name = 'temp'
    else:
        name = GetNumberOfPictures(path)
        AppendLabelFile(path, label)
    data.save(path + str(name) + '.jpg')
    return 0

def SetTempDir(path):
    _path = path + 'TEMP_DIR/'
    if os.path.isdir(_path):
        if os.path.exists(_path +'Labels.txt'):
            return 0
        os.open(_path + 'Labels.txt', os.O_CREAT)
    else:
        os.mkdir(_path)
        os.open(_path + 'Labels.txt', os.O_CREAT)
    return 0
def SaveTempLabels(path, lines):
    _path = path + 'TEMP_DIR/' + 'Labels.txt'
    f = os.open(_path, os.O_APPEND)
    if lines != []:
        with open(_path, 'w') as f:
            f.write('')
        for x in lines:
            with open(_path, 'a') as f:
                f.write(x)