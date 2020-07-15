from ImageEnhancement.claheEnhancer import equalize_light, increase_contrast, adjust_contrast
from ImageEnhancement.histogramEqualization import histEqu
from Segmentation.graphSeg import GraphSegmentation
import numpy as np
import sys
import time
import cv2
import matplotlib.pyplot as plt

path_to_image = "D:\Projects And Internships\Leaf_Counting\GraphSegPython\w6KiC.png"

# Step 1: Loading the Image Using OpenCV
image = cv2.imread(path_to_image)

# Step 2: Enhancing The Image
#image = adjust_contrast(image)
#image = equalize_light(image)
#image = increase_contrast(image)
image = histEqu(image)

# Step 3: Segmentation
segObj = GraphSegmentation(image)
segImage = segObj.BuildingTree(image)

# Step 4: Trying Something Else
'''
from PIL import Image, ImageCms
# Converting to CMYK Colour Space
segImage = cv2.cvtColor(segImage, cv2.COLOR_BGR2RGB) #BGR-> RGB
segImage = Image.fromarray(segImage) # Converting to PIL Image
segImage = segImage.convert("CMYK") # Converting RGB to CMYK Image
segImage = np.asarray(segImage) # COnverting Back to Numpy array
segImage = segImage.copy()
for i in range(segImage.shape[0]):
    for j in range(segImage.shape[1]):
        if(segImage[i][j][0]<=85):
            segImage[i][j][0] = 0
        if(segImage[i][j][1]<=15):
            segImage[i][j][1] = 0
        if(segImage[i][j][2]<=180):
            segImage[i][j][2] = 0


#srgb_p = ImageCms.createProfile("sRGB")
#lab_p  = ImageCms.createProfile("LAB")
#rgb2lab = ImageCms.buildTransformFromOpenProfiles(srgb_p, lab_p, "RGB", "LAB")
#Lab = ImageCms.applyTransform(segImage, rgb2lab)
#L, a, b = Lab.split()
#a = 0

fig, axs = plt.subplots(2, 2)
axs[0, 0].hist(segImage[:, :, 0])
axs[0, 0].set_title('Channel C')
axs[0, 1].hist(segImage[:, :, 1])
axs[0, 1].set_title('Channel M')
axs[1, 0].hist(segImage[:, :, 2])
axs[1, 0].set_title('Channel Y')
axs[1, 1].hist(segImage[:, :, 3])
axs[1, 1].set_title('Channel K')
plt.show()


#segImage = np.asarray(Lab)

#print(np.max(segImage))
'''

cv2.imshow("Leaves", segImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
