import os
from tkinter.filedialog import askdirectory
import ctypes
from shutil import copyfile
from os import path

def copyJustFiles(path,des):
    if not path or not des or path +'/' in des + '/':
        return False
    if os.path.isfile(des) or os.path.islink(des):
        return False
    if not os.path.isdir(des):
       return False
    for file in os.listdir(path):
        if os.path.isdir(path + '/' + file):
            copyJustFiles(path + '/' + file, des)
        else:
            copyfile(path + '/' + file,des + '/' +file)
    return True

if __name__ == '__main__':
    ctypes.windll.user32.MessageBoxW(0,'Please select the folder with the files in it.','Mega.Inc')
    userPath = askdirectory()
    if userPath:
        ctypes.windll.user32.MessageBoxW(0, 'Please select where you want the files to go.', 'Mega.Inc')
        userDes = askdirectory()
        if userDes:
            if copyJustFiles(userPath,userDes):
                ctypes.windll.user32.MessageBoxW(0, 'Done! Your files have been copied', 'Mega.Inc')
            else:
                ctypes.windll.user32.MessageBoxW(0, 'The was a problem copying the files. Please try again.', 'Mega.Inc')
