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


trained_model = 'models/vgg_emotion_weights_006.h5'

current_file = ""
img = None
im_label = None
label_res = None
default_pic = "default.png"
pb_1 = None
pb_2 = None
pb_3 = None
pb_l1 = None
pb_l2 = None
pb_l3 = None

categoriesEitW = ['Angry','Disgust','Fear','Happy','Neutral','Sad','Surprise']
emotion_colors = ['red','green','purple','yellow','gray','blue','orange']


print("Loading model " + trained_model+ "... ")
model = load_model(trained_model)
print("Done.")

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
	global current_file
	global label_res
	global pb_1, pb_2, pb_3
	global pb_l1, pb_l2, pb_l3
	im_input = get_image(current_file)
	print "Analyzing " + current_file + " ..."
	res = model.predict(im_input)
	print "Subject feeling ..."
	res_list = res[0].tolist()
	emotion = categoriesEitW[res_list.index(max(res_list))]
	print emotion
	label_res.configure(text=emotion, bg=emotion_colors[categoriesEitW.index(emotion)])
	res_list_sorted = list(res_list)
	res_list_sorted.sort(reverse=True)
	print res_list_sorted
	print res_list
	pb_1["value"] = res_list_sorted[0] * 100
	pb_2["value"] = res_list_sorted[1] * 100
	pb_3["value"] = res_list_sorted[2] * 100

	pb_l1.configure(text=categoriesEitW[res_list.index(res_list_sorted[0])])
	pb_l2.configure(text=categoriesEitW[res_list.index(res_list_sorted[1])])
	pb_l3.configure(text=categoriesEitW[res_list.index(res_list_sorted[2])])




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

label_fname = Label(root, text=default_pic)
label_fname.grid(row=3, column=0, columnspan=3)

pb_1 = ttk.Progressbar(root,orient ="horizontal",length = 200, mode ="determinate")
pb_1.grid(row=4, column=0, columnspan=1)
pb_1["maximum"] = 100
pb_1["value"] = 0

pb_2 = ttk.Progressbar(root,orient ="horizontal",length = 200, mode ="determinate")
pb_2.grid(row=4, column=1, columnspan=1)
pb_2["maximum"] = 100
pb_2["value"] = 0

pb_3 = ttk.Progressbar(root,orient ="horizontal",length = 200, mode ="determinate")
pb_3.grid(row=4, column=2, columnspan=1)
pb_3["maximum"] = 100
pb_3["value"] = 0

pb_l1 = Label(root, text="Cat1")
pb_l1.grid(row=5, column=0, columnspan=1)

pb_l2 = Label(root, text="Cat1")
pb_l2.grid(row=5, column=1, columnspan=1)

pb_l3 = Label(root, text="Cat1")
pb_l3.grid(row=5, column=2, columnspan=1)




root.wm_title("Uberclock EmotionDetection")
root.mainloop()
root.destroy()