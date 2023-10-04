#cadastro de pessoas, profissao e conectar essa profissional na pessoa

import sqlite3

banco = sqlite3.connect('cadastro_usuarios.db')
cursor = banco.cursor()

'''CRIAR DADOS PESSOAIS'''

# nome = "José Ruela"
# idade = 50
# email = "ruela@gmail.com"
# telefone = "6799999-9999"

cursor.execute("CREATE TABLE colaborador (id_colaborador integer primary key autoincrement nome text, idade integer, email text, tel text, foreign key profissao_id)")

# cursor.execute("INSERT INTO colaborador VALUES('"+nome+"',"+str(idade)+",'"+email+"','"+telefone+"')")
# banco.commit()

# cursor.execute("SELECT * FROM colaborador")
# print(cursor.fetchall())

'''CRIAR DADOS PROFISSIONAIS'''

# funcao = "Coordenador de Programação"
# setor = "Programação de TV"

cursor.execute("CREATE TABLE profissao (funcao text, setor text)")
# cursor.execute("INSERT INTO profissao VALUES('"+funcao+"','"+setor+"')")
# banco.commit()
# cursor.execute("SELECT * FROM profissao")
# print(cursor.fetchall())

#cursor.execute("DROP TABLE ")

