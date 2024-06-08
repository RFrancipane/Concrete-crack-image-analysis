#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Purpose: Find min and max crack widths of given 2d boolean array.
Author:  Raphael Francipane
Date:    9/11/2023
Method:  Create an array of the sum of true values along the width axis using
         numpy sum. Then use numpy.min with a crack_widths>0 boolean index
         to find the smallest non-zero crack width. Use an if statement
         with numpy any to st the minimum to zero if there is no crack.
         Then find the maximum using numpy max of the crack widths. Return 
         both values.
Data dictionary:
 [array] crack_bool  2d numpy boolean array representing concrete image with
                     air pockets removed
 [integer] width_axis  axis width is to be found for
 [array] crack_widths  Boolean array of crack widths along axes
 [integer] minimum  Minimum crack length
 [integer] maximum  Maximum crack length
"""
#import modules
import numpy as np

#Given 2d boolean array and axis, return integers for minimum and maximum 
#width of true values along axis
def min_max_crack_width(crack_bool, width_axis): 
    #crete array along axis of crack widths
    crack_widths = np.sum(crack_bool, axis=width_axis)
    #find min from array
    minimum = np.min(crack_widths[crack_widths>0])
    #Find minimum in case where no crack
    if np.any(crack_widths) == False:
        minimum = 0
    #find max from array
    maximum = np.max(crack_widths)
    #return values
    return minimum, maximum
