from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView

from database import Database

KV = '''
<ContentNavigationDrawer>

    MDList:
        

        MDNavigationDrawerItem:
            icon: "android"
            text: "CLick"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 1"

        MDNavigationDrawerItem:
            icon: "language-python"
            text: "CLick"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 2"

        MDNavigationDrawerItem:
            icon: "language-python"
            text: "CLick"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 2"
        
        MDNavigationDrawerItem:
            icon: "language-python"
            text: "CLick"
            on_press:
                root.nav_drawer.set_state("close")
                root.screen_manager.current = "scr 2"


MDScreen:

    MDTopAppBar:
        pos_hint: {"top": 1}
        elevation: 4
        title: "MDNavigationDrawer"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    MDNavigationLayout:

        MDScreenManager:
            id: screen_manager

            MDScreen:
                name: "scr 1"

                MDLabel:
                    text: "CADASTRO DE TAREFAS"
                    halign: "center"
                    pos_hint: {"center_x": .5, "center_y": .8}
                    size_hint_x: .5

                MDTextField:
                    id:nome
                    hint_text: "NOME"
                    helper_text: "Digite seu nome"
                    helper_text_mode: "on_focus"
                    pos_hint: {"center_x": .5, "center_y": .7}
                    size_hint_x: .5
                
                MDTextField:
                    id:cpf
                    hint_text: "CPF"
                    helper_text: "Digite seu CPF"
                    helper_text_mode: "on_focus"
                    pos_hint: {"center_x": .5, "center_y": .6}
                    size_hint_x: .5
                
                MDTextField:
                    id:email
                    hint_text: "E-MAIL"
                    helper_text: "Digite seu email"
                    helper_text_mode: "on_focus"
                    pos_hint: {"center_x": .5, "center_y": .5}
                    size_hint_x: .5
                
                MDTextField:
                    id:telefone
                    hint_text: "TELEFONE"
                    helper_text: "Digite seu telefone"
                    helper_text_mode: "on_focus"
                    pos_hint: {"center_x": .5, "center_y": .4}
                    size_hint_x: .5
                
                MDTextField:
                    id:endereco
                    hint_text: "ENDEREÇO"
                    helper_text: "Digite sue endereço"
                    helper_text_mode: "on_focus"
                    pos_hint: {"center_x": .5, "center_y": .3}
                    size_hint_x: .5

                MDRaisedButton:
                    id:btn_cancelar
                    text: "Cancelar"
                    md_bg_color: "red"
                    pos_hint: {"center_x": .7, "center_y": .2}
                    size_hint_x: .2
                
                MDRaisedButton:
                    id:btn_cadastrar
                    text: "Cadastrar"
                    md_bg_color: "orange"
                    pos_hint: {"center_x": .3, "center_y": .2}
                    size_hint_x: .2
                    on_press: app.cadastrar(nome.text,cpf.text,email.text,telefone.text,endereco.text)

            MDScreen:
                name: "scr 2"

                MDLabel:
                    text: "LISTA DE TAREFAS"
                    halign: "center"
            
            MDScreen:
                name: "scr 2"

                MDLabel:
                    text: "Screen 2"
                    halign: "center"
            
            MDScreen:
                name: "scr 2"

                MDLabel:
                    text: "Screen 2"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer
            radius: (0, 16, 16, 0)

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''


class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class Example(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_string(KV)
    
    def cadastrar(self,nome,cpf,email,telefone,endereco):
        db = Database()
        pessoa = [nome,cpf,email,telefone,endereco]
        enviou = db.insert(pessoa)
        print(enviou)

        
Example().run()