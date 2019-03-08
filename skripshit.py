from xml.dom import minidom
import os

datadir = '/media/chiken-eater/PELAJARAN/Data Skripsi/frame/foto plat/'
files = os.listdir(datadir)

for file in files:
    if file.endswith('.xml'):
        print(file)
        skrishit = minidom.parse(os.path.join(datadir, file))
        xmin = int(skrishit.getElementsByTagName('xmin')[0].firstChild.data)
        ymin = int(skrishit.getElementsByTagName('ymin')[0].firstChild.data)
        xmax = int(skrishit.getElementsByTagName('xmax')[0].firstChild.data)
        ymax = int(skrishit.getElementsByTagName('ymax')[0].firstChild.data)
        print(xmin)
        print(ymin)
        print(xmax)
        print(ymax)

namabahini isis something
nambah skripshit
