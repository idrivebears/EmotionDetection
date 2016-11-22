import os, glob

categoriesEitW = [ 'Angry' , 'Disgust' , 'Fear' , 'Happy'  , 'Neutral' ,  'Sad' , 'Surprise']

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

# File and label list to input to keras
f = open('datasets/training_list.txt', 'w')

# List of images to train on
# Include png for homemade images, and tiff for jaffe images
dir = 'datasets/training_images/'
imgList = glob.glob(dir+'*.png') + glob.glob(dir+'*.tiff')


for img in imgList:
    if os.path.isdir(img):
        continue
    label = get_label(img)
    fname = img.split('/')[2]
    f.write(fname + ' ' + str(label) + '\n')

f.close()
