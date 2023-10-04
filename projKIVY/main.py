from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.button import Button

class Test(App):
    def build(self):
        return Button(text='Hello World', font_size=50, color="red")
    
Test().run()


