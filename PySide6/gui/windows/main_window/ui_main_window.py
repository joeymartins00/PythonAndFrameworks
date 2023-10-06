# IMPORT QT CORE
from qt_core import *

# MAIN WINDOW - JANELA PRINCIPAL
class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # SET INITIAL PARAMETERS - DEFINIR PARÂMETROS INICIAIS
        parent.resize(1200, 720)
        parent.setMinimumSize(960, 540)

        # CREATE CENTRAL PARAMETERS - CRIAR PARÂMETROS CENTRAIS
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("background-color: #282a36")

        # CREATE MAIN LAYOUT - CRIANDO O LAYOUT PRINCIPAL
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)

        # LEFT MENU - MENU ESQUERDO
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)

        # CONTENT - CONTEÚDO
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")

        # Content Layout - Layout de Conteúdo
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)

        # TOP BAR - CABEÇALHO (BARRA SUPERIOR)
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10,0,10,0)

        # Left Label - Label Esquerda (Rótulo esquerdo)
        self.top_label_left = QLabel("Essa é minha primeira aplicação com PySide6")

        # Top Spacer - Espaçador Superior
        self.top_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum )

        # Right Label - Label Esquerda (Rótulo esquerdo)
        self.top_label_right = QLabel("| PÁGINA INICIAL")
        self.top_label_right.setStyleSheet("font: 700 9pt ' Segoe UI'")

        # Add to Layout - Adicionar ao layout        
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.top_label_right)


        # Application Pages - Páginas do aplicativo
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2;" )

        # BOTTOM BAR/FOOTER - RODAPÉ/BARRA INFERIOR
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(10,0,10,0)

        # Left Label - Label Esquerda (Rótulo esquerdo)
        self.bottom_label_left = QLabel("Criado por: Joceyr Gomes Martins")

        # Top Spacer - Espaçador Superior
        self.bottom_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum )

        # Right Label - Label Esquerda (Rótulo esquerdo)
        self.bottom_label_right = QLabel("® 2023")

        # Add to Layout - Adicionar ao layout        
        self.bottom_bar_layout.addWidget(self.bottom_label_left)
        self.bottom_bar_layout.addItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_label_right)

        # Add to Content Layout - Adicionar ao layout de conteúdo
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)

        # ADD WIDGETS TO APP - ADICIONAR WIDGETS AO APLICATIVO (ELEMENTOS DE INTERAÇÃO)
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)


        # SET CENTRAL WIDGET - DEFINIR WIDGET CENTRAL
        parent.setCentralWidget(self.central_frame)