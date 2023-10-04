from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class Test(App):
    def build(self):
        caixa = BoxLayout(orientation='vertical')
        texto = Label(text='Texto')
        botao = Button(text='Clique Aqui')



        caixa.add_widget(texto)
        caixa.add_widget(botao)
        return caixa
    
Test().run()