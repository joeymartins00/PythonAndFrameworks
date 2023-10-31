from kivymd.app import MDApp
from kivy.lang import Builder


class MeuApp(MDApp):
    def build(self):
        self.screen = Builder.load_file("load.kv")
        return self.screen
    

if __name__ == "__main__":
    MeuApp().run()