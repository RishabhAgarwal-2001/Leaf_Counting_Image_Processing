from ImageEnhancement.claheEnhancer import equalize_light, increase_contrast, adjust_contrast
from ImageEnhancement.histogramEqualization import histEqu
from Segmentation.graphSeg import GraphSegmentation
import numpy as np
import sys
import time
import cv2
import matplotlib.pyplot as plt
import argparse


parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input", required=True, help="path to input image")
parser.add_argument("-o", "--output", required=True, help="path to output image")
parser.add_argument("-p", "--process", default="2", help="Four Different Enhancement Options [1/2/3/4]")
args = vars(parser.parse_args())


#path_to_image = "D:\Projects And Internships\Leaf_Counting\GraphSegPython\ImageTest.png"

path_to_image = args["input"]
output_path = args["output"]
preprocess = args["process"]

# Step 1: Loading the Image Using OpenCV
image = cv2.imread(path_to_image)
if(type(image) is np.ndarray):
    # Step 2: Enhancing The Image
    function_dict = {'1':adjust_contrast, '2':equalize_light, '3':increase_contrast, '4':histEqu}
    image= function_dict[preprocess](image)
    
    # Step 3: Segmentation
    segObj = GraphSegmentation(image)
    segImage = segObj.BuildingTree(image)


    cv2.imwrite("Results.png", segImage)
    
else:
    print("Invalid Path to Image Given... Terminating!!!")
