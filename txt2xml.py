from xml.dom.minidom import parseString
from lxml.etree import Element
from lxml.etree import SubElement
from lxml.etree import tostring
from os.path import join
from imutils.paths import list_files
import numpy as np

import os
import imagesize
import argparse
import sys

"""
COCO annotation format: .txt files
index, x, y, w, h
ex: 0 0.487742 0.533946 0.342763 0.736917
"""

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', type=str, default='', help='contain txt file - coco annotation format')
    parser.add_argument('--output_path', type=str, default='', help='will contain xml file after converting')

    parser.add_argument('--image_path', type=str, default='', help='contain images')
    
    parser.add_argument('--class_names', default='', help=".txt or . names, contain class names of dataset, ex: dog, cat,...")
    parser.add_argument('--dataset_name', type=str, default='Coco')
    return parser.parse_args(args)


def unconvert(class_id, width, height, x, y, w, h):
    """Converts the normalized positions  into integer positions
    """
    xmax = int((x*width) + (w * width)/2.0)
    xmin = int((x*width) - (w * width)/2.0)
    ymax = int((y*height) + (h * height)/2.0)
    ymin = int((y*height) - (h * height)/2.0)
    class_id = int(class_id)
    return (class_id, xmin, xmax, ymin, ymax)


def xml_transform(classes):
    """Converts coco into xml
    """
    # List all txt annotation files
    l = list_files(args.input_path)

    # List all name of files
    ids = list()
    ids=[os.path.basename(x).split('.')[0] for x in l]
    print(ids)

    annopath = join(args.input_path, '%s.txt')
    imgpath = join(args.image_path, '%s.jpg')
    
    os.makedirs(args.output_path, exist_ok=True)
    outpath = join(args.output_path, '%s.xml')

    for i in range(len(ids)):
        img_id = ids[i] 
        width, height = imagesize.get(imgpath % img_id)

        node_root = Element('annotation')
        node_folder = SubElement(node_root, 'folder')
        node_folder.text = args.dataset_name
        img_name = img_id + '.jpg'
    
        node_filename = SubElement(node_root, 'filename')
        node_filename.text = img_name
        
        node_source= SubElement(node_root, 'source')
        node_database = SubElement(node_source, 'database')
        node_database.text = 'Coco database'
        
        node_size = SubElement(node_root, 'size')
        node_width = SubElement(node_size, 'width')
        node_width.text = str(width)
    
        node_height = SubElement(node_size, 'height')
        node_height.text = str(height)

        node_depth = SubElement(node_size, 'depth')
        node_depth.text = str(3) #channels

        node_segmented = SubElement(node_root, 'segmented')
        node_segmented.text = '0'

        target = (annopath % img_id)
        if os.path.exists(target):
            label_norm= np.loadtxt(target).reshape(-1, 5)

            for i in range(len(label_norm)):
                labels_conv = label_norm[i]
                new_label = unconvert(labels_conv[0], width, height, labels_conv[1], labels_conv[2], labels_conv[3], labels_conv[4])
                node_object = SubElement(node_root, 'object')
                node_name = SubElement(node_object, 'name')
                node_name.text = classes[new_label[0]]
                
                node_pose = SubElement(node_object, 'pose')
                node_pose.text = 'Unspecified'
                
                
                node_truncated = SubElement(node_object, 'truncated')
                node_truncated.text = '0'
                node_difficult = SubElement(node_object, 'difficult')
                node_difficult.text = '0'
                node_bndbox = SubElement(node_object, 'bndbox')
                node_xmin = SubElement(node_bndbox, 'xmin')
                node_xmin.text = str(new_label[1])
                node_ymin = SubElement(node_bndbox, 'ymin')
                node_ymin.text = str(new_label[3])
                node_xmax = SubElement(node_bndbox, 'xmax')
                node_xmax.text =  str(new_label[2])
                node_ymax = SubElement(node_bndbox, 'ymax')
                node_ymax.text = str(new_label[4])
                xml = tostring(node_root, pretty_print=True)  
                dom = parseString(xml)
        f =  open(outpath % img_id, "wb")
        f.write(xml)
        f.close()     


def main(args):
    # Read class names of dataset
    with open(args.class_names) as f:
        class_names = f.read().splitlines()

    xml_transform(class_names)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    print('\ninput_path=',args.input_path)
    print('output_path=',args.output_path)
    print('class_names=',args.class_names)
    print('image_path=',args.image_path)
    print('dataset_name=',args.dataset_name, '\n')
    main(args)