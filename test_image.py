#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

This file uses a real image to test 
    concrete_image_to_bool()
    remove_air_pockets()
    concrete_image_analysis()

The best way to use this file is to run the code in the cells one-by-one.  

"""

import concrete_image_to_bool as img2bool 
import remove_air_pockets as remove
import concrete_image_analysis as ana
import matplotlib.pyplot as plt 
import numpy as np

# %% Constants 
# The given image is a coloured image that has brightness in red, green and 
# blue (RGB) colour spectra. We only need greyscale image. This numpy array 
# is used to convert RGB colour scale to greyscale. 
RGB_to_GREYSCALE = [0.2126,0.7152,0.0722] # Convert red-green-blue 

# %% Load the test image and extra a block it for testing

# Load the image 
concrete_image_rbg = plt.imread('test_image.jpg') 
# A coloured image is a 3-d numpy array with shape (290, 402, 3)

# Convert the coloured image to greyscale
concrete_image_greyscale = np.sum(concrete_image_rbg * RGB_to_GREYSCALE, 
                                  axis = 2)  

# Slice a (50, 97) block for testing 
concrete_image = concrete_image_greyscale[:50, 200:297]

# Plot the concrete image
fig = plt.figure()
plt.imshow(concrete_image, cmap = 'gray', vmin = 0, vmax = 255)
plt.title('Real concrete image in greyscale')
plt.colorbar()
plt.show()

# %% Input values and expected answers

# Input values
threshold = 100
max_pocket_len = 7
width_axis = 1

# Expected answers
# The expected concrete_bool and crack_bool are stored in test_ref_data.npz
ref_data = np.load('test_ref_data.npz', allow_pickle = True)
expected_concrete_bool = ref_data['expected_concrete_bool']
expected_crack_bool = ref_data['expected_crack_bool']

expected_extent_0, expected_extent_1  = 50, 91 
expected_min_width, expected_max_width = 55, 62

# %% To test concrete_image_to_bool()

# Run your concrete_image_to_bool
your_concrete_bool = img2bool.concrete_image_to_bool(concrete_image,threshold)

fig, axs = plt.subplots(2, 1, sharex = True)
axs[0].imshow(your_concrete_bool, cmap = 'gray_r', vmin = 0, vmax = 1)
axs[0].set_title('Your concrete_bool')
axs[1].imshow(expected_concrete_bool, cmap = 'gray_r', vmin = 0, vmax = 1)
axs[1].set_title('The expected concrete_bool')
plt.show()

# Compare your_concrete_bool and expected_concrete_bool
if np.all(your_concrete_bool == expected_concrete_bool):
    print('Your concrete_image_to_bool returned the correct result')
else:
    print('Your concrete_image_to_bool did NOT return the correct result')

# %% To test your remove_air_pockets()

# Run your remove_air_pockets()
your_crack_bool = remove.remove_air_pockets(your_concrete_bool, max_pocket_len)

fig, axs = plt.subplots(2, 1, sharex = True)
axs[0].imshow(your_crack_bool, cmap = 'gray_r', vmin = 0, vmax = 1)
axs[0].set_title('Your crack_bool')
axs[1].imshow(expected_crack_bool, cmap = 'gray_r', vmin = 0, vmax = 1)
axs[1].set_title('The expected crack_bool')
plt.show()

# Compare your_crack_bool and expected_crack_bool
if np.all(your_crack_bool == expected_crack_bool):
    print('Your remove_air_pockets returned the correct result')
else:
    print('Your remove_air_pockets() did NOT return the correct result')


# %% To test your concrete_image_analysis()

# Run your concrete_image_analysis()
your_extent_0, your_extent_1, your_min_width, your_max_width = \
        ana.concrete_image_analysis(concrete_image, threshold, max_pocket_len,
                                    width_axis)

# Create lists to do the comparisons
expected_answer = \
    [expected_extent_0, expected_extent_1,
     expected_min_width, expected_max_width]
    
your_answer = [your_extent_0, your_extent_1, 
               your_min_width, your_max_width]

output_names = \
    ['extent_0','extent_1','min_width','max_width']

for k in range(len(output_names)):
    # Print the purpose and answers  
    print('For the computation of the',output_names[k],':')
    print('\tYour function returns',your_answer[k])
    print('\tThe expected answer is',expected_answer[k])
    
    if type(your_answer[k]) in [int, np.int64, np.int32]:
        if your_answer[k] == expected_answer[k]:
            print('\tYour',output_names[k],'is correct')
        else:
            print('\tYour',output_names[k],'is NOT correct') 
    else:
        print('\tYour',output_names[k],'does not have the correct type') 

    print('')       
        
 

        

         