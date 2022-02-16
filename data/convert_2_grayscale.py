import argparse
import os
import cv2
import numpy as np
from PIL import Image
from numpy import dtype

parser = argparse.ArgumentParser(description='Coverts training data insto grayscale')
parser.add_argument('-input_dir', type=str, help='Path to directory containing images to be split into train, test and val')
parser.add_argument('-format_converter', type=str, help='Input image colorformat - rgb2bgr, bgr2rgb, rgb2gray, bgr2gray, gray2rgb, gray3bgr')
parser.add_argument('-output_dir', type=str, help='Path to directory containing images to be split into train, test and val')

color_conversions = {'rgb2bgr':4, 'bgr2rgb':4, 'rgb2gray':7, 'bgr2gray':6, 'gray2rgb':8, 'gray2bgr':8}


args = parser.parse_args()


#TODO:Add checks for valid color conversions
def main(args):
    color_read_enum = 1
    color_convert_enum = color_conversions[args.format_converter]
    if color_convert_enum == 8:
        color_read_enum = 0
    try:
        os.mkdir(args.output_dir)
    except:
        pass
    for filename  in os.listdir(args.input_dir):
        img_path = os.path.join(args.input_dir, filename)
        img = cv2.imread(img_path,color_read_enum)
        converted_img = cv2.cvtColor(img, color_convert_enum)
        output_img_path = os.path.join(args.output_dir, filename)
        cv2.imwrite(output_img_path, converted_img)
        


if __name__ == "__main__":
    main(args)
