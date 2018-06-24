import os
import os.path


def extract_txt(file_path, output):

    files = os.listdir(file_path)
    current_frame = 1

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

                next_frame = current_frame + 4

                if next_frame < frames_num:
                    write_folder = 'train/' + folder[-3] + '/' + folder[-2] + ' 1' + ' ' + str(current_frame) + ' ' + str(frames_num) + '\n'
                    current_frame = current_frame + 4
                    print(write_folder)

                    writefile = open(output, "a")
                    writefile.writelines(write_folder)
                    writefile.close()

                if next_frame >= frames_num:
                    current_frame = 1
                    break




path = "/home/moliheng/Deep-Feature-Flow/data/SCUT_FIR/Data/VID/train"
output = "/home/moliheng/Deep-Feature-Flow/data/SCUT_FIR/VID_frame.txt"

extract_txt(path, output)
