# Python GUI for EmotionDetection

from Tkinter import *


def load_image():
	print "hello"

def analyze_image(f_name):
	print "analyzing: " + f_name




root = Tk()
root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(480, 320))


label_res = Label(root, text="Result: ", bg="white")
label_res.pack(fill=X)
button = Button(root, text="QUIT", command=root.quit)
button.pack(side=LEFT)
load_image = Button(root, text="Load Image", command=load_image)
load_image.pack(side=LEFT)
button = Button(root, text="Analyze")
button.pack(side=LEFT)

root.mainloop()
root.destroy()