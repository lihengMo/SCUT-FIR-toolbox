import os
import os.path


def xml_del(file_path,det_str):


    files = os.listdir(file_path)
    print(len(files))

    for name in files:

        subpath = os.path.join(file_path,name)
        if os.path.isdir(subpath):

            print subpath
            xml_del(subpath,det_str)

        if not os.path.isdir(name):

            folder = subpath.split('/')

            tmpp = folder[-3][0]
            if tmpp == 's':

                print(name)
                old = open(os.path.join(file_path, name))
                print old
                lines = old.readlines()

                newlines = []
                for line in lines:
                    if det_str in line:
                        line = line.replace(det_str, "")
                        print('replaced')

                    newlines.append(line)

                new = open(os.path.join(file_path, name), "w")
                new.writelines(newlines)
                new.close()
                old.close()


str ='<?xml version="1.0" ?>'

path = "/home/moliheng/Deep-Feature-Flow/data/SCUT_FIR/Annotations/VID/train"

xml_del(path, str)