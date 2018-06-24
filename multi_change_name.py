import os
import os.path


def xml_del(file_path):


    files = os.listdir(file_path)
    print(len(files))

    for name in files:

        subpath = os.path.join(file_path,name)
        if os.path.isdir(subpath):

            print (subpath)
            xml_del(subpath)

        if not os.path.isdir(name):

            folder = subpath.split('/')

            tmpp = folder[-3][0]
            if tmpp == 's':

                print(name)

                newname = '0' + name[1:]

                print(newname)
                os.rename(os.path.join(file_path, name), os.path.join(file_path, newname))
                #print(name)
                #old = open(os.path.join(file_path, name))
                #print(old)





path = "/home/moliheng/Deep-Feature-Flow/data/SCUT_FIR/Data/VID/train"

xml_del(path)