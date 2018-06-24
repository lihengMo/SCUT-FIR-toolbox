import os
import os.path

totalframe_num = 1

def extract_txt(file_path, output):

    files = os.listdir(file_path)

    print(len(files))
    global totalframe_num

    for name in files:

        subpath = os.path.join(file_path,name)
        if os.path.isdir(subpath):

            print(subpath)
            extract_txt(subpath, output)

        if not os.path.isdir(name):
            folder = subpath.split('/')

            tmpp = folder[-3][0]
            if tmpp == 's':
                frames_num = len(files)

                file_name = folder[-1].split('.')

                write_folder = 'val/' + folder[-3] + '/' + folder[-2] + '/' + file_name[0] + ' ' + str(totalframe_num) + '\n'
                print(write_folder)

                totalframe_num = totalframe_num + 1

                writefile = open(output, "a")
                writefile.writelines(write_folder)
                writefile.close()






path = "/home/moliheng/Deep-Feature-Flow/data/SCUT_FIR/Data/VID/val"
output = "/home/moliheng/Deep-Feature-Flow/data/SCUT_FIR/VID_val_frames.txt"

extract_txt(path, output)
