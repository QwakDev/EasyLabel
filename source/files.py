import tkinter as tk
import os


def AppendLabelFile(): #TODO file of labels in .txt matching files in DIR  LABEL1,LABEL2,LABEL3...
    return 0
def GetNumberOfFiles(): #TODO count number of files in dir
    return 0
def GetListOfFiles(path): #TODO Make sure they are files, FUTURE filtering
    out = []
    if os.path.isdir(path):
        _listOfFiles = os.listdir(path)
        for i in _listOfFiles:
            out.append(i)
    else:
        out = False
    return out
def ReadFile(dir, file):#TODO read img and return it IN THE FUTURE transform
    return 0
def SetSavingDir(path):#TODO (*create dir AND LabelFile) OR (return number of files and labels) OR Output of wrong path given
    if os.path.isdir(path):
        if os.path.exists(path + 'Label.txt'):
            print('path exists')
    else:
        os.mkdir(path)
        os.open(path + 'Label.txt', 'a+')
    return 0
def SaveFile(data, label): #TODO save img to <x>.btm x=1,2,3... AND append label file with label
    return 0


