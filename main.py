# Source
# https://www.analyticsvidhya.com/blog/2022/06/cartoonify-image-using-opencv-and-python/

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
    gray_scale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    resized_two = cv2.resize(gray_scale_image(960,540))
    
    #apply medium blur to smoothen an image
    smooth_gray_scale = cv2.medianBlur(gray_scale_image, 5)
    resized_three = cv2.resize(smooth_gray_scale, (960,540))
    
    # edges
    get_edge = cv2.adaptive_threshold(smooth_gray_scale, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,9,9)
    resized_four = cv2.resize(get_edge, (960,540))
    
    # bilateral filter
    color_image = cv2.bilateralFilter(original_image, 9, 300,300)
    resized_five = cv2.resize(color_image(960,540))
    
    #masking
    cartoon_image = cv2.bitwise_and(color_image, color_image, mask = get_edge)
    resized_six = cv2.resize(cartoon_image, (960, 540))
    

# upload image from local system
def upload():
    image_path = easygui.fileopenbox()
    #cartoonify(image_path)