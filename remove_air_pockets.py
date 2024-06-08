#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Purpose: Remove air pockets from 2d boolean array
Author:  Raphael Francipane
Date:    9/11/2023
Method:  Use max_pocket_len + 2 to find the size of squares to be checked in
        is_an_air_pocket. Then use a numpy ndenumerate for loop with array
        slicing to loop over all top left corners of squares to be checked by
        is_an_air_pocket. Using array slicing, check if these squares are air
        pockets, and if true, use array slicing to change the inside of the 
        square to false. Once all squares have been checked, return the 
        modified array.
    Loop over all possible pockets of max length, and if the array
         segment is an air pocket, change all values inside it to false
Data dictionary:
 [array] concrete_bool  2d numpy boolean array representing concrete image
 [integer] max_pocket_len  Max size of an air pocket
 [integer] sqr_len  Square size to be input to is_an_air_pocket function
                    defined as max_pocket_len + 2
"""
#import modules
import numpy as np
import is_an_air_pocket as is_pocket

#Given 2d boolean array and max pocket length, remove all air pockets in array 
#as defined by is_an_air_pocket function and return modified array
def remove_air_pockets(concrete_bool, max_pocket_len):
    #define length of squares taken for testing
    sqr_len = 2 + max_pocket_len
    #for all top left corners of square
    for (x,y), value in np.ndenumerate(concrete_bool[:-sqr_len+1,:-sqr_len+1]):
        #make square false if it is an air pocket
        if is_pocket.is_an_air_pocket(concrete_bool[x:x+sqr_len,
                                                    y:y+sqr_len]) == True:
            concrete_bool[x:x+sqr_len,y:y+sqr_len] = False
    #return modified array
    return concrete_bool
            
        
    
    
