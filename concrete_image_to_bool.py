#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Purpose: Convert greyscale 2d array to 2d boolean array based on a threshold
Author:  Raphael Francipane
Date:    9/11/2023
Method:  Create a numpy array of greyscale values strictly less than threshold
         using numpy boolean logic
Data dictionary:
 [array] concrete_image  2d numpy greyscale array representing concrete image
 [float] threshold  Threshold for boolean image (any value less than is true)
 [array] concrete_bool  2d numpy boolean array representing concrete image
"""
#import modules
import numpy as np 

#use 2d greyscale array to generate true false boolean, where pixel is true
#if value of array less than threshold value
def concrete_image_to_bool(concrete_image, threshold):  
    #create boolean numpy array from values less than threshold
    concrete_bool = concrete_image < threshold
    return concrete_bool
