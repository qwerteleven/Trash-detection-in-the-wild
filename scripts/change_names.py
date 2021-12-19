

import os

# Getting the current work directory (cwd)
thisdir = os.getcwd() + "/dataset"
print(thisdir)
path = []
filename = []

# r=root, d=directories, f = files
for r, d, f in os.walk(thisdir):
    d.sort(key=lambda x: int(x.split("_")[-1]))
    for file in sorted(f, key=lambda x: int(x.split(".")[0])):
        
        if file.endswith(".jpg"):
            path.append(os.path.join(r, file))
        if file.endswith(".JPG"):
            path.append(os.path.join(r, file))


count = 0

for file_path in path:
    os.rename(file_path, "/".join(file_path.split("/")[:-1]) + "/" + str(count) + ".jpg")
    count = count + 1




