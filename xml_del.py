import os
import os.path

a='<?xml version="1.0" ?>'

path = "/home/moliheng/Deep-Feature-Flow/data/SCUT_FIR/Annotations/DET"
files = os.listdir(path)
print(len(files))

for name in files:
    if not os.path.isdir(name):
        print(name)
        old = open(os.path.join(path, name))
        lines = old.readlines()

        newlines = []
        for line in lines:
            if a in line:
                line = line.replace(a, "")
                print('replaced')

            newlines.append(line)

        new = open(os.path.join(path, name), "w")
        new.writelines(newlines)
        new.close()
        old.close()



