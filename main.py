import cv2
import numpy
import easygui
import imageio
import matplotlib
import os
import tkinter

def cartoonify(image_path):
    original_image = cv2.imread(image_path)
    original_imag = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

# upload image from local system
def upload():
    image_path = easygui.fileopenbox()
    #cartoonify(image_path)