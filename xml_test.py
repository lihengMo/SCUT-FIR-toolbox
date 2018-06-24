# coding=utf-8
import os
import os.path
import xml.dom.minidom

path = "/home/moliheng/annotations"
files = os.listdir(path)  # 得到文件夹下所有文件名称
s = []
for xmlFile in files:  # 遍历文件夹
    if not os.path.isdir(xmlFile):  # 判断是否是文件夹,不是文件夹才打开
        print(xmlFile)

        # TODO
    # xml文件读取操作

    # 将获取的xml文件名送入到dom解析
    dom = xml.dom.minidom.parse(os.path.join(path, xmlFile))  ###最核心的部分os.path.join(path,xmlFile),路径拼接,输入的是具体路径
    root = dom.documentElement
    # 获取标签对name/pose之间的值
    apath = root.getElementsByTagName('path')

    # 重命名class name
    for i in range(len(apath)):
        print(apath[i].firstChild.data)
        apath[i].firstChild.data = 'VOCtoyota'
        print(apath[i].firstChild.data)

        # 保存修改到xml文件中
    with open(os.path.join(path, xmlFile), 'w') as fh:
        dom.writexml(fh)
        print('写入name/pose OK!')
