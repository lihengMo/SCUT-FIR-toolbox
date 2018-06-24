import os.path
import shutil



file = open('/home/moliheng/Deep-Feature-Flow/data/SCUT_FIR/datasets/extract02/annotations/set00/V001/I00467.txt')

lines = file.readlines()

for line in lines:
    line = line.split(' ')
    if line[0] =='ride_person':
        x,y,w,h = line[1],line[2],line[3],line[4]

    if line[0] =='walk_person' :
        x,y,w,h = line[1],line[2],line[3],line[4]

    print(line)
