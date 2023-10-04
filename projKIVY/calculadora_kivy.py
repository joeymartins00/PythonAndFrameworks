
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
import math


class FuckingCalculator(App):
    def build(self):
        container = BoxLayout(orientation='vertical')

        self.top = Label(text='RESULTADO', on_press=self.reset, font_size=30)

        header = BoxLayout(orientation ='horizontal')
        self.bot1 = Button(text='7', font_size=30, on_press= lambda x:self.click('7'))
        self.bot2 = Button(text='8', font_size=30,  on_press= lambda x:self.click('8'))
        self.bot3 = Button(text='9', font_size=30,  on_press= lambda x:self.click('9'))
        self.botmais = Button(text="+", font_size=30, on_press= lambda x:self.click('+'))
        self.botsla = Button(text="<<", font_size=30, on_press= lambda x:self.click('<<'))


        header.add_widget(self.bot1)
        header.add_widget(self.bot2)
        header.add_widget(self.bot3)
        header.add_widget(self.botmais)
        header.add_widget(self.botsla)

        main = BoxLayout(orientation ='horizontal')
        self.bot4 = Button (text='4', font_size=30,  on_press= lambda x:self.click('4'))
        self.bot5 = Button (text='5', font_size=30,  on_press= lambda x:self.click('5'))
        self.bot6 = Button (text='6', font_size=30,  on_press= lambda x:self.click('6'))
        self.botsub = Button (text='-', font_size=30, on_press= lambda x:self.click('-'))
        self.both = Button (text='^', font_size=30, on_press= lambda x:self.click('^'))
        
        main.add_widget(self.bot4)
        main.add_widget(self.bot5)
        main.add_widget(self.bot6)
        main.add_widget(self.botsub)
        main.add_widget(self.both)

        footer = BoxLayout(orientation ='horizontal')
        self.bot7 = Button (text='1', font_size=30,  on_press= lambda x:self.click('1'))
        self.bot8 = Button (text='2', font_size=30,  on_press= lambda x:self.click('2'))
        self.bot9 = Button (text='3', font_size=30,  on_press= lambda x:self.click('3'))
        self.botX = Button (text='X', font_size=30, on_press= lambda x:self.click('*'))
        self.botR = Button (text='√', font_size=30, on_press= lambda x:self.raiz('√'))

        
        footer.add_widget(self.bot7)
        footer.add_widget(self.bot8)
        footer.add_widget(self.bot9)
        footer.add_widget(self.botX)
        footer.add_widget(self.botR)

        footer2 = BoxLayout(orientation ='horizontal')
        self.bot10 = Button (text='C', font_size=30, on_press=self.reset)
        self.bot11 = Button (text='0', font_size=30,  on_press= lambda x:self.click('0'))
        self.bot12 = Button (text='#', font_size=30, on_press= lambda x:self.click('#'))
        self.botaoDivisao = Button (text='/', font_size=30, on_press= lambda x:self.click('/'))
        self.botaoIgual = Button (text='=', font_size=30, on_press=self.calcular)

        
        footer2.add_widget(self.bot10)
        footer2.add_widget(self.bot11)
        footer2.add_widget(self.bot12)
        footer2.add_widget(self.botaoIgual)
        footer2.add_widget(self.botaoDivisao)

        container.add_widget(self.top)
        container.add_widget(header)
        container.add_widget(main)
        container.add_widget(footer)
        container.add_widget(footer2)
        

        return container

    def reset(self,lbl):
        self.top.text = ""


    def click(self, text):
        self.top.text += text

    def raiz(self, text):
        result = (int(self.top.text))**0.5
        self.top.text = str(result)

    def calcular(self, text):
        if '*' in self.top.text:
            valor = self.top.text.split("*")
            self.top.text = str(int(valor[0])*int(valor[1]))
            print(valor)
    
        elif '/' in self.top.text:
            valor = self.top.text.split("/")
            self.top.text = str(int(valor[0])/int(valor[1]))
            print(valor)
    
        elif '+' in self.top.text:
            valor = self.top.text.split("+")
            self.top.text = str(int(valor[0])+int(valor[1]))
            print(valor)
    
        elif '-' in self.top.text:
            valor = self.top.text.split("-")
            self.top.text = str(int(valor[0])-int(valor[1]))
            print(valor)
    
        elif '^' in self.top.text:
            valor = self.top.text.split("^")
            self.top.text = str(int(valor[0])**int(valor[1]))
            print(valor)


FuckingCalculator().run()