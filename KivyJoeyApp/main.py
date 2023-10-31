from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import MDList,OneLineAvatarIconListItem,IconLeftWidget,IconRightWidget
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.label import Label
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.scrollview import MDScrollView
from kivy.properties import ObjectProperty

from database import Database

import uuid

# banco = Database()

# banco.insert()

class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class Headbanger(MDApp):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.alldata = []
		self.mydialog = None


	def build(self):
		self.screen = Builder.load_file("load.kv")
		return self.screen

	# CRIAR FUNÇÃO PARA ADICIONAR ALGO À LISTA DE TAREFAS
	def addnewtodo(self,value):
		print("YOu input is = ",value)
		if value :
			# CRIAR UUID PARA EDITAR E EXCLUIR (UUID é um objeto único que não se repete)
			item_id = str(uuid.uuid4())
			self.alldata.append(
				{"value":value,"id":item_id}
				)

			# OBTER ID DO ARQUIVO KV MDLIST
			todo_list = self.screen.ids.todo_list
			# E ADICIONAR AO WIDGET NO SELETOR de todo_list
			todo_list.add_widget(
				OneLineAvatarIconListItem(
					IconLeftWidget(
						icon="pencil",
						on_release=lambda x:self.editbtn(item_id,value)
						),
					IconRightWidget(
						icon="delete",
						on_release=lambda x:self.deletebtn(item_id)
						),
					id=item_id,
					text=value
					)

				)

		# E LIMPAR O TEXTO DE ENTRADA APÓS CLICAR NO BOTÃO ADICIONAR
		self.screen.ids.inputtodo.text = ""



	def editbtn(self,dataid,value):
		print("You Id FOr edit is ",dataid)
		self.editcontent = MDTextField(hint_text="update name",mode="fill")
		self.mylayout = MDBoxLayout(
			orientation="vertical",
			size_hint_y=0.8,
			height=300
			)
		# ADICIONAR EDITCONTENT AO LAYOUT BOXLAYOUT
		self.mylayout.add_widget(Label(text="edit data"))
		if not self.mydialog:
			self.dialog = MDDialog(
				title="edit data",
				type="custom",
				size_hint=(0.8,None),
				height=300,
				content_cls=self.mylayout,
				buttons=[
					MDFlatButton(
						text="save",
						text_color="red",
						on_release=lambda x:self.savenow(dataid,self.editcontent.text)

						)

				]

				)
		self.dialog.content_cls.add_widget(self.editcontent)
		self.dialog.open()

	def savenow(self,data,newvalue):
		# E SE FOR SUCESSO EDITAR ENTÃO MOSTRAR SNACKBAR
		self.notif = Snackbar(
			bg_color=(0,0,1,1)

			)

		# E FECHE SUA EDIÇÃO DE DIÁLOGO
		self.dialog.dismiss()

		# E AGORA EDITAR self.alldata edit IN textfiled edit
		for x in self.alldata:
			if x['id'] == data:
				# os dados são ID DA SUA LISTA 
				x['value'] = newvalue

				# E OBTER ID DA LISTA DE TAREFAS DO ARQUIVO KV
				todo_list = self.screen.ids.todo_list
				for child in todo_list.children:
					if child.id == data:
						child.text = newvalue

						# E MOSTRAR SNACKBAR
						self.notif.open()





	def deletebtn(self,data):
		# LOOP self.alldata E CHECAR SE id == id de dados e removeit
		for x in self.alldata:
			if x['id'] == data:
				self.alldata.remove(x)
				print(self.alldata)

				# E LISTA O ITEM NO ARQUIVO KV REMOVE OS DADOS DE ATUALIZAÇÃO
				todo_list = self.screen.ids.todo_list
				for child in todo_list.children:
					if child.id == data:
						todo_list.remove_widget(child)
					# OS DADOS SÃO ID UNIQ DE UUID4







if __name__ == "__main__":
	Headbanger().run()