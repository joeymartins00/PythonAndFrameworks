import tkinter
import sqlite3

# #Criando o Banco de Dados
# conexao = sqlite3.connect("cliente.db")

# #Criando o Cursor -> É a mesma coisa que o método construtor
# cursor = conexao.cursor()

# # #Criar a Tabela
# # cursor.execute("CREATE TABLE clientes(nome text, email text, telefone text)")

# #Commit -> A função commit envia as mudanças ou criações para o banco de dados.
# conexao.commit()

# #fechar a conexão com o banco
# conexao.close()

#Criar a Janela -> É o ambiente onde serão inseridas as informações

janela = tkinter.Tk()
janela.geometry("330x350")
janela.title("fabrica276")

#Função de cadastrar cliente

def cadastrar_cliente():
    conexao = sqlite3.connect("cliente.db")
    cursor = conexao.cursor()


    #Inserir os dados na tabela
    cursor.execute("INSERT INTO clientes VALUES (:nome, :email, :telefone)",
                {
                    "nome":entry_nome.get(),
                    "email":entry_email.get(),
                    "telefone":entry_telefone.get()
                }
                )
    
    conexao.commit()
    conexao.close()

    #Apaga os dados das caixas de entrada -> "Inputs"
    entry_nome.delete(0, "end")
    entry_email.delete(0, "end")
    entry_telefone.delete(0, "end")



#Nome dos campos -> "LABELS"

label_nome = tkinter.Label(janela, text="Nome")
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_email = tkinter.Label(janela, text="E-mail")
label_email.grid(row=1, column=0, padx=10, pady=10)

label_telefone = tkinter.Label(janela, text="Telefone")
label_telefone.grid(row=2, column=0, padx=10, pady=10)


#Caixas de entra -> "INPUTS - (Entry)"

entry_nome = tkinter.Entry(janela, width=35)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

entry_email = tkinter.Entry(janela, width=35)
entry_email.grid(row=1, column=1, padx=10, pady=10)

entry_telefone = tkinter.Entry(janela, width=35)
entry_telefone.grid(row=2, column=1, padx=10, pady=10)

#Botões -> "BUTTON"

btn_cadastrar = tkinter.Button(text="CADASTRAR", command=cadastrar_cliente)
btn_cadastrar.grid(row=3, column=0, columnspan=2, padx=10, pady=10,ipadx=80) #Columnspan usado para centralizar o botão entre as linhas a partir do zero
                                                                             #Ipadx é usado para mostrar o tamanho interno do botão.





janela.mainloop()