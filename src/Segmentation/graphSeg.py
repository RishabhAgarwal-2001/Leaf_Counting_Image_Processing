import numpy as np
import sys
import time
import cv2
class GraphSegmentation:
    source = []
    terminal = []
    graph = []
    Theta_H = []
    Theta_S = []
    Theta_V = []
    Theta = []
    P = None
    H = 0
    W = 0
    def __init__(self, image):
        image = self.convertNormalize(image)
        self.createGraphNodes(image)
        self.establishEdges(image)
        self.updateParameters(image)
        #self.weightPredictionParameter(image)
        print("Initiation Completed!!!")
        # self.assignCost(image)


    def convertNormalize(self, image):
        image = np.float32(image)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        image[:, :, 0] = image[:, :, 0]/360
        image[:, :, 2] = image[:, :, 2]/255
        return image
    
    # Graph Build
        
    def createGraphNodes(self, image):
        '''
        Function to Create Graph Structure
        Each node has its own adjacency list
        Initially all are empty
        '''
        print("Creating Graph Nodes....")
        self.H, self.W, _ = image.shape # Extracting the number of Horizontal and Vertical Pixels in the image
        for row in range(self.H):
            self.graph.append([])
            for col in range(self.W):
                self.graph[row].append([])  # For each pixel, create an empty list
        print("Number of Adj. List Created = ", self.H*self.W)
        print("Graph Node Creation Completed!!!")

    def establishEdges(self, image):
        '''
        Function to Establish Edges in The graph
        Edges are established as described in The Papers
        '''
        print("Establising Edges...")
        for i in range(self.H):
            for j in range(self.W):
                if(i+1<self.H): # If (i+1, j)th node exists then create a link with weight -1
                    self.graph[i][j].append([i+1, j, -1])
                    self.graph[i+1][j].append([i, j, -1])
                if(j+1<self.W): # If (i, j+1)th node exists then create a link with weight -1
                    self.graph[i][j].append([i, j+1, -1])
                    self.graph[i][j+1].append([i, j, -1])
                self.graph[i][j].append(['S', 'S', -1])
                self.source.append([i, j, -1])
                self.graph[i][j].append(['T', 'T', -1])
                self.terminal.append([i, j, -1])
        print("Edge Establishment Completed Successfully!!!")
        return

    
    def updateParameters(self, image):
        '''
        Function to mark nodes with permissible values of H, S and V Plane
        All nodes with permissible H value are appended in theta_H
        All nodes with permissible S value are appended in theta_S
        All nodes with permissible V value are appended in theta_V
        '''
        print("Updating Theta Values")
        # Permissible values
        min_H = 0.17
        max_H = 0.4
        min_S = 0.2
        max_S = 1
        min_V = image[:, :, 2].mean()
        max_V = 1
        self.P = []
        for i in range(self.H):
            self.P.append([])
            for j in range(self.W):
                h_val = image[i, j, 0]
                s_val = image[i, j, 1]
                v_val = image[i, j, 2]
                valid = 0
                if(h_val>=min_H and h_val<=max_H):
                    self.Theta_H.append([i, j])
                    valid = valid + 1
                if(s_val>=min_S and s_val<=max_S):
                    self.Theta_S.append([i, j])
                    valid = valid + 1
                if(v_val>=min_V and v_val<=max_V):
                    self.Theta_V.append([i, j])
                    valid = valid + 1
                if(valid==3):
                    self.Theta.append([i, j])
                    self.P[i].append(1)
                else:
                    self.P[i].append(0)
        print("Theta Values Updated!!!")
        print("Number of Valid Points = ", len(self.Theta), "out of", self.H*self.W)
        print("Weight Prediction Parameter Building Completed!!!")
        return
    
    def weightPredictionParameter(self, image):
        '''
        Function to Create the Weight Prediction Parameter
        The prediction parameter P has the same size as that of the image
        P has value either 0 or 1
        '''
        print("Building Weight Prediction Parameter...")
        #self.P = np.zeros(shape=(self.H, self.W))
        self.P = []
        for i in range(self.H):
            self.P.append([])
            for j in range(self.W):
                print(i, ", ", j)
                if([i, j] in self.Theta):
                    self.P[i].append(1)
                else:
                    self.P[i].append(0)
        print("Building Weight Prediction Completed!!!")
        return

    def assignCost(self, image):
        '''
        Function to assign cost to edges based on the value
        of prediction parameter calaculated.
        '''
        for i in range(self.H):
            for j in range(self.W):
                for edges in self.graph[i][j]:
                    if(edges[0] not in ['S', 'T']):
                        if(self.P[i][j]==1 and self.P[edges[0]][edges[1]]==1):
                            edges[2] = 0
                        else:
                            edges[2] = 1
                    if(edges[0]=='S'):
                        if(self.P[i][j]==1):
                            edges[2] = 0
                        else:
                            edges[2] = 1
                    if(edges[0]=='T'):
                        if(self.P[i][j]==0):
                            edges[2] = 0
                        else:
                            edges[2] = 1
        for edges in self.source:
            if(self.P[edges[0]][edges[1]]==1):
                edges[2] = 0
            else:
                edges[2] = 1
        for edges in self.terminal:
            if(self.P[edges[0]][edges[1]]==1):
                edges[2] = 1
            else:
                edges[2] = 0
        return

    def BuildingTree(self, image):
        for i in range(self.H):
            for j in range(self.W):
                if(self.P[i][j]==0):
                	image[i, j] = [0, 0, 0]
        return image

    
            
            
        

# image = [[[0.1, 0.1, 0.1], [0.2, 0.4, 0.6]],
#          [[0.21, 0.34, 0.56], [0.34, 0.78, 0.99]],
#          [[0.11, 0.22, 0.33], [0.34, 0.78, 0.99]]]
# image = np.array(image).reshape((3, 2, 3))
# # print(image)
# obj = GraphSegmentation(image)
# # obj.process(image)

# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# import matplotlib.colors as colors
# image = mpimg.imread('img.png', 0)
# image = colors.rgb_to_hsv(image)
#import cv2
#image = cv2.imread('D:\Projects And Internships\Leaf_Counting\GraphSegPython\imge.jpeg')

#image = np.float32(image)
#image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#image[:, :, 0] = image[:, :, 0]/360
#image[:, :, 2] = image[:, :, 2]/255
#image = cv2.resize(image, (300, 300))
#obj = GraphSegmentation(image)
#image = obj.heuristic(image)
#cv2.imshow("Bhagwan G", image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
#green = image[:, :, 1].copy()
#red = image[:, :, 2].copy()
#image[:, :, 1] = red
#image[:, :, 2] = green

#cv2.imshow("Bhagwan G", image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
