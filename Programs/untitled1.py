import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang import builder
from kivy.uix.tabbedpanel import TabbedPanel

def callback(instance):
	print(' The button <%s> is being pressed' % instance.text)

class Test():
	btn1 = Button(text='1'  , font_size = 14)
	btn1.bind(on_presses = callback)
	btn2 = Button(text = '2' , font_size = 14)
	btn2.bind(on_press = callback)

class MainApp(App):
	def build(self):
		return Test()
		
if __name__ == '__main__':
	MainApp().run()
