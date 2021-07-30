import json
import argparse
import os
import shutil

from numpy.lib.type_check import imag

parser = argparse.ArgumentParser(description='Splits COCO annotations file into training and test sets.')
parser.add_argument('-val', type=str, help='Path to validation annotations')
parser.add_argument('-train', type=str, help='Path to training annotations ')
parser.add_argument('-test', type=str, help='Path to testing annotations')
parser.add_argument('-input_dir', type=str, help='Path to directory containing images to be split into train, test and val')

args = parser.parse_args()

def save_images(images, parent_dir, annotation_type):
    folder_path = os.path.join(parent_dir,annotation_type)
    os.mkdir(folder_path)
    for image in images:
        input_path = os.path.join(parent_dir, "images/"+image['file_name'])
        output_path = os.path.join(folder_path, image['file_name'])
        print(input_path)
        shutil.copy(input_path, output_path)

def main(args):
    parent_dir = args.input_dir
    annotations_dict = {"train":os.path.join(parent_dir, args.train), "test":os.path.join(parent_dir, args.test), "val":os.path.join(parent_dir, args.val)}
    for key, annotations in annotations_dict.items():
        with open(annotations, 'rt', encoding='UTF-8') as ann:
            coco = json.load(ann)
            images = coco['images']
            save_images(images, args.input_dir, key)
            

if __name__ == "__main__":
    main(args)