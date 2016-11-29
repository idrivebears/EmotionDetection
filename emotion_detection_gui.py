# Python GUI for EmotionDetection

from Tkinter import *
from Tkinter import Tk
import ttk
from tkFileDialog import askopenfilename
from functools import partial
from PIL import ImageTk, Image
from load_data import get_image

from keras.models import Sequential, load_model
from keras.layers import Dense, Convolution2D, MaxPooling2D, Activation, Flatten, Dropout
from load_data import load_images
from keras import backend as K
K.set_image_dim_ordering('th')
from keras.utils import np_utils
import numpy as np
from scipy import ndimage
from scipy import misc


current_file = ""
img = None
im_label = None
default_pic = "default.png"
pb = None

print("Creating model")
model = load_model('models/vgg_emotion_weights_006.h5')

def load_image():
	global current_file
	global img
	global im_label
	filename = askopenfilename() 
	img = ImageTk.PhotoImage(Image.open(filename))
	im_label.configure(image=img)
	im_label.image = img
	label_fname.configure(text=filename)
	current_file = filename


def analyze_image():
	im_input = get_image(current_file)
	print "Analyzing " + current_file + " ..."
	res = model.predict(im_input)
	print res

root = Tk()
root.resizable(width=True, height=True)
#root.geometry('{}x{}'.format(800, 620))

img = ImageTk.PhotoImage(Image.open(default_pic))
im_label = Label(root, image = img)
im_label.grid(row=0, column = 1 )

quit_b = Button(root, text="QUIT", command=root.quit)
quit_b.grid(row=1, column=0)
load_image = Button(root, text="Load Image", command=load_image)
load_image.grid(row=1, column = 1)
analyze = Button(root, text="Analyze", bg="#90ff84", activebackground="#48ce39", command=analyze_image)
analyze.grid(row=1, column=2)

label_res = Label(root, text="Result: ", bg="white")
label_res.grid(row=2, column = 0, columnspan=3)

pb = ttk.Progressbar(root,orient ="horizontal",length = 200, mode ="determinate")
pb.grid(row=4, column=0, columnspan=3)
pb["maximum"] = 100
pb["value"] = 0

label_fname = Label(root, text=default_pic)
label_fname.grid(row=3, column=0, columnspan=3)


root.wm_title("Uberclock EmotionDetection")
root.mainloop()
root.destroy()