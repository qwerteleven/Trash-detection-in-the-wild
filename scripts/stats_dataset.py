import os
import shutil

img = []
labels = []
n_super_class
n_class = 0
n_instances = 0
resolution = 0


# Getting the current work directory (cwd)
thisdir = os.getcwd()

# r=root, d=directories, f = files
for r, d, f in os.walk(thisdir):
    for file in f:
        instance = os.path.join(r, file)
        
        if file.endswith(".jpg"):
            img.append('/'.join(instance.split("/")[-2:]).split(".")[0])
          

        if file.endswith(".txt"):
            labels.append('/'.join(instance.split("/")[-2:]).split(".")[0])


