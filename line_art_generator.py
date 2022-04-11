#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 22:37:18 2022

@author: ssaini
"""

from PIL import Image, ImageDraw, ImageChops
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from random import randint, random
import colorsys


image_size_px = None
padding_px = None

def show_image(image_path):
    img = mpimg.imread(image_path)
    plt.imshow(img)
    plt.axis('off')
    plt.show()

def generate_points(total_line):
    global image_size_px, padding_px
    
    line_points = []
    for count in range(total_line*2):
        line_points.append(randint(padding_px, image_size_px[0]-padding_px))
        
    # print(line_points)
    return line_points

def generate_color(start_color, end_color, factor):
    recip = 1 - factor
    return (
        int(start_color[0] * recip + end_color[0] * factor),
        int(start_color[1] * recip + end_color[1] * factor),
        int(start_color[2] * recip + end_color[2] * factor)
        )    
               
    #line_colors.append(end_color)
    
    return line_colors

def randcolor():
    h = random()
    s = 1
    v = 1
    rgb = [int(n*255) for n in colorsys.hsv_to_rgb(h, s, v)]
    
    return tuple(rgb)
    
def generate_art(image_path):
    print('Generating Art!')
    global image_size_px, padding_px
    image_size_px = (500, 500)
    padding_px = 50
    image_bg_color = (0, 0, 0)
    image = Image.new("RGB", image_size_px, image_bg_color)
    
    draw = ImageDraw.Draw(image)
    
    total_line = 10
    thickness = 3
    line_end_points = None
    
    start_color = randcolor() 
    end_color = randcolor()
    color_factor = 5
    
    line_points = generate_points(total_line)
    
    # bounding box
    min_xpoint = min(line_points[::2])
    max_xpoint = max(line_points[::2])
    min_ypoint = min(line_points[::-2])
    max_ypoint = max(line_points[::-2])
    # draw.rectangle((min_xpoint, min_ypoint, max_xpoint, max_ypoint), outline=(255, 0, 0))
    
    bb_centroid = ((max_xpoint-min_xpoint)/2 + min_xpoint, (max_ypoint-min_ypoint)/2 + min_ypoint)
    img_centroid = (image_size_px[0]/2, image_size_px[1]/2)
    # draw.line((bb_centroid[0], bb_centroid[1], img_centroid[0], img_centroid[1]), fill=(0,0,0), width=5)
    extra_xlen = bb_centroid[0]-img_centroid[0]
    extra_ylen = bb_centroid[1]-img_centroid[1]
    #draw.rectangle((min_xpoint - extra_xlen, min_ypoint - extra_ylen, max_xpoint - extra_xlen, max_ypoint - extra_ylen), outline=(255, 0, 0))
    
    factor = 1
    
    for count in range(total_line-1):
        
        # overlay
        overlay_image = Image.new("RGB", image_size_px, image_bg_color)
        overlay_draw = ImageDraw.Draw(overlay_image)
        
        line_point = (line_points[count+(count*factor)] - extra_xlen, line_points[(count+1)+(count*factor)] - extra_ylen, line_points[(count+2)+(count*factor)] - extra_xlen, line_points[(count+3)+(count*factor)] - extra_ylen)
                
        overlay_draw.line(line_point, generate_color(start_color, end_color, count*factor/10), thickness)
        image = ImageChops.add(image, overlay_image)
        thickness += 3
        
    image.save(image_path)
    show_image(image_path)
    
if __name__ == '__main__':
    for n in range(10):
        generate_art(f'test_{n}.png')