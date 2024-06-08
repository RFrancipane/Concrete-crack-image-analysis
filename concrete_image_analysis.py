#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Purpose: Analyse a given greyscale crack image to find the crack extents, and
         minimum and maximim widths along a given axis.
Author:  Raphael Francipane
Date:    9/11/2023
Method:  Use concrete_to_bool to convert the concrete image and threshold to a
         2d boolean array concrete_bool. crack_bool is then generated by 
         removing air pockets of the given max length from concrete_bool 
         using remove_air_pockets. cack_extent is then used on both axes to 
         find the two extents of the crack, and min_max_crack width is used 
         to find the min and max crack length along the width axis.
Data dictionary:
 [array] crack_bool  2d numpy boolean array representing concrete image with
                     air pockets removed
 [integer] max_pocket_len  Maximum square size of an air pocket expected
                           in the concrete.
 [float] threshold  Threshold for boolean image (any value less than is true)
 [integer] width_axis Axis width should be found along
 [array] concrete_bool  2d numpy boolean array representing concrete image
 [array] crack_bool 2d numpy boolean array, concrete_bool with cracks removed
 [integer] extent_0 extent of crack along axis 0
 [integer] extent_1 extent of crack along axis 1
 [integer] minimum minimum crack length along width_axis
 [integer] maximum maximum crack length along width_axis
"""
#import modules
import crack_extent as extent
import min_max_crack_width as crack_width
import remove_air_pockets as remove_air
import concrete_image_to_bool as concrete_to_bool

#given greyscale 2d image array, threshold, max air pocket length and width 
#axis, return integer extents and minimum/maximum lengths of a crack in image
def concrete_image_analysis(concrete_image, threshold, max_pocket_len,
                            width_axis): 
    #convert image to boolean
    concrete_bool = concrete_to_bool.concrete_image_to_bool(concrete_image, 
                                                            threshold)   
    #remove air pockets
    crack_bool = remove_air.remove_air_pockets(concrete_bool, max_pocket_len)
    #find extents and min/max
    extent_0 = extent.crack_extent(crack_bool, 0)
    extent_1 = extent.crack_extent(crack_bool, 1)
    minimum, maximum = crack_width.min_max_crack_width(crack_bool, width_axis)
    #return data
    return extent_0, extent_1, minimum, maximum
