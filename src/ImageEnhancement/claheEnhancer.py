import cv2
import numpy as np
import matplotlib.pyplot as plt

def equalize_light(image, limit=3, grid=(7,7), gray=False):
    if (len(image.shape) == 2):
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
        gray = True
    
    clahe = cv2.createCLAHE(clipLimit=limit, tileGridSize=grid)
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    cl = clahe.apply(l)
    limg = cv2.merge((cl,a,b))

    image = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    if gray: 
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("Light Equalization Completed!!!")
    return np.uint8(image)

def increase_contrast(image):
    
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    l, a, b = cv2.split(lab)

    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)

    limg = cv2.merge((cl, a, b))

    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    print("Contrast Enhancement Completed!!!")
    return final 


def adjust_contrast(imrgb):
    clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(2,2))

    imrgb[:,:,0] = clahe.apply(imrgb[:,:,0])
    imrgb[:,:,1] = clahe.apply(imrgb[:,:,1])
    imrgb[:,:,2] = clahe.apply(imrgb[:,:,2])
    print("Contrast Adjusted Successfully!!!")
    return imrgb

