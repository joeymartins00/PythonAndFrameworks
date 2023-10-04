from PyQt6 import uic, QtWidgets
import pymysql.connections

banco = pymysql.connections.Connection(
    host = "localhost",
    user = "root",
    password = "",
    database = "cadastro276"

)

def cadastrar_usuario():
    nome = form_usuario.nome.text()
    email = form_usuario.email.text()
    telefone = form_usuario.telefone.text()
    matricula = form_usuario.matricula.text()


    if (form_usuario.coordenador.isChecked()):
        perfil = "Coordenador"
    elif (form_usuario.estudante.isChecked()):
        perfil = "Estudante"
    elif (form_usuario.professor.isChecked()):
        perfil = "Professor"
    

    cursor = banco.cursor()
    sql = "INSERT INTO usuarios(nome, email, telefone, matricula, perfil) VALUES (%s,%s,%s,%s,%s)"
    dados = (str(nome), str(email), str(telefone), str(matricula), perfil)
    cursor.execute(sql, dados)
    banco.commit()

    form_usuario.nome.setText("")
    form_usuario.email.setText("")
    form_usuario.telefone.setText("")
    form_usuario.matricula.setText("")

def listar_dados():
    listar_usuario.show()

    cursor = banco.cursor()
    sql = "SELECT * FROM usuarios"
    cursor.execute(sql)
    dados_recebidos = cursor.fetchall()

    listar_usuario.tableWidget.setRowCount(len(dados_recebidos))
    listar_usuario.tableWidget.setColumnCount(6)

    for linha in range(0, len(dados_recebidos)):
        for coluna in range(0, 6):
            listar_usuario.tableWidget.setItem(linha, coluna, QtWidgets.QTableWidgetItem(str(dados_recebidos[linha][coluna])))

app = QtWidgets.QApplication([])
form_usuario = uic.loadUi("usuario.ui")
listar_usuario = uic.loadUi("listar_dados.ui")
form_usuario.cadastrar.clicked.connect(cadastrar_usuario)
form_usuario.listar.clicked.connect(listar_dados)

form_usuario.show()
app.exec()