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

def get_image(dir):
    if os.path.isdir(dir):
        print "Please pick one image only."
    em_image = misc.imread(image_dir, mode='L')
    image_arr = np.zeros((count, 1, 256, 256))
    return image_arr

def load_images(dir):

    image_inputs = []
    image_outputs = []
    print "Dataset to be loaded:"
    print os.listdir(dir)
    
    x = raw_input("Key to continue")
    count = len(os.listdir(dir))

    for im in os.listdir(dir):

        if os.path.isdir(im):
            continue
        image_dir = dir + "/" + im
        em_image = misc.imread(image_dir, mode='L')
        label = get_label(image_dir)
        image_inputs.append(em_image)
        image_outputs.append(label)

    input_arr = np.zeros((count, 1, 256, 256))
    output_arr = np.zeros(count)

    for i in range(0, count):
        output_arr[i] = image_outputs[i]
    
    for i in range(0,  count):
        input_arr[i] = image_inputs[i]

    return (input_arr, output_arr)











