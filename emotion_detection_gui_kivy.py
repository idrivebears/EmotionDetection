import kivy 
kivy.require('1.0.0')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class ImageViewer(GridLayout):
    def __init__(self, **kwargs):
        super(ImageViewer, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Image'))

        self.image_container = Image(source='datasets/test_images/KA.AN1.39.tiff')
        self.add_widget(self.image_container)

        self.analyze_button = button = Button(text='Analyze...', font_size=14)
        self.add_widget(self.analyze_button)


class MyApp(App):
	title = 'Uberclock ITESO : EmotionDetection'

	def build(self):
		return ImageViewer()


if __name__ == '__main__':
    MyApp().run()