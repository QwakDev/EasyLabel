import tkinter as tk
import os

def GetLabels(path):
    out = []
    return
def AppendLabelFile(path): #TODO file of labels in .txt matching files in DIR  LABEL1,LABEL2,LABEL3...
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
def SetSavingDir(path):#TODO  OR Output of wrong path given
    if os.path.isdir(path):
        if os.path.exists(path + 'Label.txt'):
            return len(GetListOfFiles(path)) - 1
        os.open(path + 'Label.txt', os.O_CREAT)
        return len(GetListOfFiles(path)) - 1
    else:#CREATING NEW DIR
        os.mkdir(path)
        os.open(path + 'Label.txt', os.O_CREAT)
        return 0
    
def SaveFile(data, label): #TODO save img to <x>.btm x=1,2,3... AND append label file with label
    return 0


SetSavingDir('D:\Projects\EasyLabel\data_save_test/')