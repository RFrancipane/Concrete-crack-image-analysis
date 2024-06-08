#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Purpose: Determine whether a given 2d boolean array is an air pocket
Author:  Raphael Francipane
Date:    9/11/2023
Method:  Test if there are any true values inside the inner square of an array
         copy using numpy any and array slicing. If false, then not a pocket,
         If true, overwrite the innersquare to false using the same method, 
         and check if there are any true values remaining. If so, then there 
         must be a true in the outer ring, so it is not an air pocket, else it 
         is an air pocket. 
Data dictionary:
 [array] square_patch  2d boolean array input
 [array] square_patch_copy copy of square_patch modified to check if pocket
 [boolean] is_pocket  True if square_patch is an air pocket, else false
"""
#import modules
import numpy as np 

#return true if outer edge of 2d array is false and there is at least one true
#inside inner square
def is_an_air_pocket(square_patch):  
    #modifying original array affects data used to call function, use copy
    #to not modify concrete array in remove_air_pockets
    square_patch_copy = square_patch.copy()
    #if any black squares in inner square
    if np.any(square_patch_copy[1:-1,1:-1]) == False:
        is_pocket = False
        #not pocket if no black in inner square
    else:
        #overwrite inner square to not effect detection of outer square
        square_patch_copy[1:-1,1:-1] = False
        #test if any black in outer square
        if np.any(square_patch_copy) == True:
            is_pocket = False
        #tests passed so pocket
        else:
            is_pocket = True
    return is_pocket