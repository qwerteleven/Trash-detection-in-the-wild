import os
import shutil

import cv2 as cv

# Getting the current work directory (cwd)
thisdir = os.getcwd()

# r=root, d=directories, f = files
for r, d, f in os.walk(thisdir):
    for file in f:
        instance = os.path.join(r, file)
        
        if file.endswith(".jpg"):
            img = cv.imread(instance)
            if img.shape[0] or img.shape[1] < 720:
                os.remove(instance)
            

        if file.endswith(".JPG"):
            img = cv.imread(instance)
            if img.shape[0] or img.shape[1] < 720:
                os.remove(instance)

        if file.endswith(".png"):
            img = cv.imread(instance)
            if img.shape[0] or img.shape[1] < 720:
                os.remove(instance)

        if file.endswith(".PNG"):
            img = cv.imread(instance)
            if img.shape[0] or img.shape[1] < 720:
                os.remove(instance)
            


