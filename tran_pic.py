import shutil
import os
import os.path

path = "/home/moliheng/annotations"
files = os.listdir(path)
print(len(files))

for name in files:
    #print(name)
    oldname = name.split('.')
    #print(oldname)
    if len(oldname) == 3:
        newname = oldname[0]+'.'+oldname[1]
        print(newname)
        os.rename(os.path.join(path, name), os.path.join(path, newname))
        print('renamed')
