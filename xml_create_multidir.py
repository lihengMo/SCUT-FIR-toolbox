from lxml.etree import Element, SubElement, tostring
import pprint
from xml.dom.minidom import parseString
import os.path
import shutil

#path = "/home/moliheng/Deep-Feature-Flow/data/SCUT_FIR/datasets/extract05/annotations"

def xml_create(file_path):

    files = os.listdir(file_path)

    for txtfile in files:

        subpath = os.path.join(file_path, txtfile)
        if os.path.isdir(subpath):


            xml_create(subpath)

        if not os.path.isdir(txtfile):
            print(txtfile)

            folder = subpath.split('/')

            out_folder = folder[-3] + '_' + folder[-2]

            tmpp = folder[-3][0]
            if tmpp == 's':

                print(out_folder)

                filename = folder[-1].split('.')

                tmp2 = filename[0].split('I')
                n_filename = '0' + tmp2[1]

                node_root = Element('annotation')

                node_folder = SubElement(node_root, 'folder')
                node_folder.text = out_folder

                node_filename = SubElement(node_root, 'filename')
                node_filename.text = n_filename

                node_source = SubElement(node_root, 'source')
                node_database = SubElement(node_source, 'database')
                node_database.text = 'SCUT_FIR'

                node_size = SubElement(node_root, 'size')
                node_width = SubElement(node_size, 'width')
                node_width.text = '720'
                node_height = SubElement(node_size, 'height')
                node_height.text = '576'

                open_file = open(os.path.join(file_path, txtfile))
                lines = open_file.readlines()

                for line in lines:
                    line = line.split(' ')
                    if line[0] == 'ride_person':
                        xmin, ymin, w, h = line[1], line[2], line[3], line[4]
                        xmax = int(xmin) + int(w)
                        ymax = int(ymin) + int(h)

                        node_object = SubElement(node_root, 'object')
                        node_name = SubElement(node_object, 'name')
                        node_name.text = 'person'
                        node_bndbox = SubElement(node_object, 'bndbox')
                        node_xmin = SubElement(node_bndbox, 'xmin')
                        node_xmin.text = str(xmin)
                        node_ymin = SubElement(node_bndbox, 'ymin')
                        node_ymin.text = str(ymin)
                        node_xmax = SubElement(node_bndbox, 'xmax')
                        node_xmax.text = str(xmax)
                        node_ymax = SubElement(node_bndbox, 'ymax')
                        node_ymax.text = str(ymax)

                    if line[0] == 'walk_person':
                        xmin, ymin, w, h = line[1], line[2], line[3], line[4]
                        xmax = int(xmin) + int(w)
                        ymax = int(ymin) + int(h)

                        node_object = SubElement(node_root, 'object')
                        node_name = SubElement(node_object, 'name')
                        node_name.text = 'person'
                        node_bndbox = SubElement(node_object, 'bndbox')
                        node_xmin = SubElement(node_bndbox, 'xmin')
                        node_xmin.text = str(xmin)
                        node_ymin = SubElement(node_bndbox, 'ymin')
                        node_ymin.text = str(ymin)
                        node_xmax = SubElement(node_bndbox, 'xmax')
                        node_xmax.text = str(xmax)
                        node_ymax = SubElement(node_bndbox, 'ymax')
                        node_ymax.text = str(ymax)

                    # print(line)

                xml = tostring(node_root, pretty_print=True)
                dom = parseString(xml)
                # print xml

                output_path = '/home/moliheng/Deep-Feature-Flow/data/SCUT_FIR/Annotations/VID/train/' + folder[-3] + '/' + \
                              folder[-2] + '/' + n_filename + '.xml'
                # print(output_path)

                fo = open(output_path, 'w')
                dom.writexml(fo)



path = "/home/moliheng/Deep-Feature-Flow/data/SCUT_FIR/datasets/extract01/annotations"


xml_create(path)