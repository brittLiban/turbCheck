import os                # Helps us work with folders and file paths
import cv2               # OpenCV: used to load and manipulate images
import numpy as np       # NumPy: helps with array/matrix operations
import matplotlib.pyplot as plt  # To display images if needed

IMG_SIZE = 224 # Resizing each img to 224x224 pixels THE CONSTANT
#can adjust this as needed for speed 
#cnns need images to be the same size! 
DATA_DIR = "data/TB_Chest_Radiography_Database"  # where the imgs are located
BAD_DATA = "data/TB_Chest_Radiography_Database/Unreadble"


#this is a function on literally going through each image inside of the tb folder lol! Or based on the given parameter folder we pass in! 
def load_images(data_dir):
    images = []  #hold images
    labels = [] #hold 0 or 1s

    for label, category in enumerate(['Normal', 'Tuberculosis']):
        path = os.path.join(data_dir, category) # it will .../Normal
        for img_file in os.listdir(path): #looping through all image files
            try:
                img_path = os.path.join(path, img_file) #now its appending the current file to the end of the path var
                img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE) #loading images in grayscale
                img = cv2.resize(img, (IMG_SIZE, IMG_SIZE)) #making it to 244 x 244
                images.append(img) #adding it to the images arr
                labels.append(label) #adding it to the labels arr
            except Exception as e:
                print(f"Could not read image {img_file}")
                os.rename(img_file, BAD_DATA)
    return np.array(images), np.array(labels) #the images are LITERALLY converted into an array (a grid of numbers)
                                              # each pixel is assigned a number 0 to 255/ each pixel has 3 numbers, r g b, 0 - 255
                                              # each image in the array has a corresponding label. They are in the same spot on their corresponsding data structures. So 1 image to 1 label! 

x,y = load_images(DATA_DIR) #this will return the arr of img as x and the corresponding id/label as y

#handling the img(arr)
x = x / 255.0 # this is to help the CNN learn faster, 0.0 us black, 0.5 is gray and 1.0 is white

x = x.reshape(-1, IMG_SIZE, IMG_SIZE, 1)
        # -1 tells NumPy to automatically figure out the number of images (batch size)
        # The two IMG_SIZEs represent the height and width of each image
        # 1 is the number of channels — use 1 for grayscale, 3 for RGB (color)

        # This reshaping ensures the data matches the expected input shape for CNNs:
        # (batch_size, height, width, channels)

        
print("image shape: ", x.shape)
print("Label Shape: ", y.shape)



    

