'''
Load all images into an array
'''
from scipy import ndimage
from scipy import misc
import numpy as np
import os 


categoriesEitW = ['Angry','Disgust','Fear','Happy','Neutral','Sad','Surprise']

jaffe_categories_map = {
    'HA': categoriesEitW.index('Happy'),
    'SA': categoriesEitW.index('Sad'),
    'NE': categoriesEitW.index('Neutral'),
    'AN': categoriesEitW.index('Angry'),
    'FE': categoriesEitW.index('Fear'),
    'DI': categoriesEitW.index('Disgust'),
    'SU': categoriesEitW.index('Surprise')
    }

def get_label(fname):
    label = fname.split('.')[1][0:2]
    return jaffe_categories_map[label]

def load_images(dir):

    image_inputs = []
    image_outputs = []
    print "Dataset to be loaded:"
    print os.listdir(dir)
    
    x = raw_input("Key to continue")

    for im in os.listdir(dir):

        if os.path.isdir(im):
            continue
        image_dir = dir + "/" + im
        em_image = misc.imread(image_dir)
        label = get_label(image_dir)
        image_inputs.append(em_image)
        image_outputs.append(label)

    return (image_inputs, image_outputs)
