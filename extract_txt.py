import os
import os.path


path = "/home/moliheng/Deep-Feature-Flow/data/SCUT_FIR/Annotations/DET"
filepath = "/home/moliheng/Deep-Feature-Flow/data/SCUT_FIR/DET_frame.txt"
files = os.listdir(path)
print(len(files))

for name in files:
    if not os.path.isdir(name):
        #print(name)
        filename = name.split('.')
        filename_out = filename[0]+' 1'+'\n'

        print(filename_out)
        writefile = open(filepath, "a")
        writefile.writelines(filename_out)
        writefile.close()


        #new = open(os.path.join(path, name), "w")
        #new.writelines(newlines)
        #new.close()
        #old.close()



