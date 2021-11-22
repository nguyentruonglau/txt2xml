# TXT 2 XML [![CircleCI](https://circleci.com/gh/faustomorales/keras-ocr.svg?style=shield)](https://github.com/nguyentruonglau) [![Documentation Status](https://readthedocs.org/projects/keras-ocr/badge/?version=latest)](https://github.com/nguyentruonglau)

All codes assume running from root directory. Please update the sys path at the beginning of the codes before running.

## Over View

Txt2Xml tool will help you convert from txt COCO format to VOC xml format in Object Detection Problem. In sample folder is valid set of Mask Wearing Dataset from [Roboflow](https://public.roboflow.com/object-detection/mask-wearing/1).


## Requirements
```
python == 3.X
tensorflow == 2.X
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
