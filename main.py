
import cv2
import numpy
import easygui
import imageio
import matplotlib
import os
import tkinter

def cartoonify(image_path):
    original_image = cv2.imread(image_path)
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    
    if original_image is None:
        print("")
        os.exit()
    
    resized_one = cv2.resize(original_image(960,540))

# upload image from local system
def upload():
    image_path = easygui.fileopenbox()
    #cartoonify(image_path)