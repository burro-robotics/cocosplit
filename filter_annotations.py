import argparse
import os
import cv2
import numpy as np
import funcy
import json
# from cocosplit import filter_annotations, save_coco 

parser = argparse.ArgumentParser(description='CReates a json file with annotations of images present in input_dir')
parser.add_argument('-input_dir', type=str, help='Path to directory containing images we want to use for deeplearning')
parser.add_argument('-annotation', type=str, help='path to the .json file containing original annotations')


args = parser.parse_args()

def get_img_list():
    img_list = [filename for filename in os.listdir(args.input_dir)]
    return img_list

def save_coco(file, info, licenses, images, annotations, categories):
    with open(file, 'wt', encoding='UTF-8') as coco:
        json.dump({ 'info': info, 'licenses': licenses, 'images': images, 
            'annotations': annotations, 'categories': categories}, coco, indent=2, sort_keys=True)

def filter_annotations(annotations, images):
    image_ids = funcy.lmap(lambda i: int(i['id']), images)
    return funcy.lfilter(lambda a: int(a['image_id']) in image_ids, annotations)

def main(args):
    print(args.annotation)
    with open(args.annotation, 'rt', encoding='UTF-8') as annotations:
        coco = json.load(annotations)
        info = coco['info']
        licenses = coco['licenses']
        images = coco['images']
        annotations = coco['annotations']
        categories = coco['categories']

        img_list = get_img_list()

        images = funcy.lremove(lambda i:i["file_name"] not in img_list, images)

        save_coco(os.path.join(args.input_dir, "annotation.json"), info, licenses, images, filter_annotations(annotations, images), categories)



if __name__ == "__main__":
    
    main(args)