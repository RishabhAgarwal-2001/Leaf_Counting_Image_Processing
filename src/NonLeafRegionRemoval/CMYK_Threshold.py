import cv2
import numpy as np
from PIL import Image

def CMYK_Thresh(image):
    '''
    Thresholding Image Based on CMYK Channels
    Prameters:
    image: BGR Image, numpy array
    '''
    RGB_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    PIL_image = Image.fromarray(RGB_image)
    PIL_image = PIL_image.convert("CMYK")
    PIL_image.save("BeforeThresh.jpeg")
    CMYK_array = np.asarray(PIL_image)
    cv2.imshow("Original", CMYK_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    thresh_C = 85
    thresh_M = 15
    thresh_Y = 180
    thresh_K = 0.4
    image_array = CMYK_array.copy()
    for i in range(image_array.shape[0]):
        for j in range(image_array.shape[1]):
            #if(image_array[i][j][0]<thresh_C):
             #   image_array[i][j][0] = 0
            #if(image_array[i][j][1]<thresh_M):
             #   image_array[i][j][1] = 0
            if(image_array[i][j][2]<thresh_Y):
                image_array[i][j][2] = 0
            if(image_array[i][j][3]<thresh_K):
                image_array[i][j][3] = 0
    PIL_image = Image.fromarray(image_array)
    PIL_image = PIL_image.convert("RGB")
    PIL_image.save("AfterThresh.jpeg")
    final_image = np.asarray(PIL_image)
    cv2.imshow("Final Image", final_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return image_array

image = cv2.imread("D:\Projects And Internships\Leaf_Counting\GraphSegPython\img_out.png")
CMYK_Thresh(image)
