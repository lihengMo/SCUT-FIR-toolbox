import os.path
import shutil

path = "/home/moliheng/RFCN-tensorflow/data/toyota/JPEGImages"

moving_path_val = "/home/moliheng/RFCN-tensorflow/data/toyota/valtoyota"

file = open('/home/moliheng/RFCN-tensorflow/data/toyota/ImageSets/Main/val.txt')

lines = file.readlines()

for line in lines:
    line = line.strip('\n')
    print(line)
    oldpos = path+'/'+line+'.jpg'
    print(oldpos)
    newpos = moving_path_val+'/'+line+'.jpg'
    print(newpos)
    shutil.move(oldpos, newpos)
    print('moved')
