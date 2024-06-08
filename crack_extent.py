#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Purpose: Determine extent of crack from 2d boolean array in a given axis
Author:  Raphael Francipane
Date:    9/11/2023
Method:  Use np.any along the opposite of the given axis(1-axis) to create a
         boolean array describing if the axis contains a true value. Sum these
         true values using numpy sum to find the extent along the given axis.
Data dictionary:
 [array] crack_bool  2d numpy boolean array representing concrete image with
                     air pockets removed
 [integer] axis_to_use  axis extent is to be found for
 [array] axis_contains_true  Boolean array of axes that contain a true value
 [integer] extent  Extent of crack along given axis
"""
#import modules
import numpy as np

#Given 2d boolean array, return the integer extent of true values along a 
#given axis
def crack_extent(crack_bool, axis_to_use): 
    #find extent by counting number of rows/columns with >1 crack segment 
    extent = np.sum(np.any(crack_bool,axis=1-axis_to_use))
    return extent