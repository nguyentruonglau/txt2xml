# TXT 2 XML [![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/) [![Documentation Status](https://readthedocs.org/projects/keras-ocr/badge/?version=latest)](https://github.com/nguyentruonglau)

All codes assume running from root directory. Please update the sys path at the beginning of the codes before running.

## Over View

Txt2Xml tool will help you convert from txt COCO format to VOC xml format in Object Detection Problem. In sample folder is valid set of Mask Wearing Dataset from [Roboflow](https://public.roboflow.com/object-detection/mask-wearing/1).


## Requirements
```
imutils==0.5.4
lxml==4.6.3
imagesize==1.2.0
```

## Execution

```
> python txt2xml.py --input_path (directory contain txt files)
                    --output_path (directory will contain xml files)
                    --image_path (contain images, get imagesize of images)
                    --class_name (class names)
                    --datataset_name (optional, name of dataset)
```

## Comment
Give me a star if you find Json2Xml useful to you.
