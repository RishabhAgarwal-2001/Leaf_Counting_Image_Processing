from ImageEnhancement.claheEnhancer import equalize_light, increase_contrast, adjust_contrast
from Segmentation.graphSeg import GraphSegmentation
import numpy as np
import sys
import time
import cv2
import matplotlib.pyplot as plt

path_to_image = "D:\Projects And Internships\Leaf_Counting\GraphSegPython\imagea.jpg"

# Step 1: Loading the Image Using OpenCV
image = cv2.imread(path_to_image)

# Step 2: Enhancing The Image
#image = adjust_contrast(image)
#image = equalize_light(image)
#image = increase_contrast(image)
cv2.imshow("Enhanced", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Step 3: Segmentation
segObj = GraphSegmentation(image)
segImage = segObj.BuildingTree(image)

cv2.imshow("Leaves", segImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
