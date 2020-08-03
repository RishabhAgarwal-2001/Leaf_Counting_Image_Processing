# Graph Based Image Segmentation
### Introduction
With increased reliance on plants for food and fuel, researchers need to use advanced technological methods to allow agricultural practices to continue without any breach. One of the biggest requirement is to increase the efficiency and yield of the crop, with an aim to enhance the throughput from a piece of land. Plant’s growth and yield are directly attributed to the number of leaves it has. Various methods are employed to count the leaves in an image. This report explores the usage of graph-segmentation to extract leaf regions from an image. The method has the advantage of minimal computation time and robustness to external factors such as brightness and contrast, which can affect the results obtained from using ConvNets and other methods. 

### Preprocessing Image
Before proceeding to image segmentation, we perform some preprocessing. The main aim is to equalize the contrast in the image and highlight the leaves in the image. The equalization algorithm used was the histogram equalization. The result of this equalization is then used in segmentation. Various other methods such as CLAHE enhancement were also tried to improve image contrast, though best results were obtained using Histogram Equalization. Below is the comparison of two methods - Left (Histogram Equalization) and Right (CLAHE).

![Image](Images/image.jpg)
