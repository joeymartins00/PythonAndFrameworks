from typing import Any
import mysql.connector

class Database():
    def __init__(self, banco="tasks") -> None:
        self.banco = banco




    def connect(self):
        self.conn = mysql.connector.connect(host='192.168.22.9',database=self.banco, user="fabrica", password="fabrica@2022")
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("Conectado ao Servidor com  sucesso!", db_info)
        else:
            print("Erro ao conectar!!!")




    def insert(self, tarefa):
        self.connect()
        # nome = "Levar o cachorro para passear"
        # desc = "Au Au"
        # data = "2023-11-11"
        # estado = "A fazer"

        try:
            self.cursor.execute("INSERT INTO JOCEYR (nome, descricao, data_tarefa, estado_tarefa) VALUES (%s,%s,%s,%s)", (tarefa[0],tarefa[1],tarefa[2],tarefa[3]))
            self.conn.commit()
        except Exception as err:
            print(err)

        finally:
            self.close_connection()




    def select(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM JOCEYR")
            result = self.cursor.fetchall()
          

            for tarefa in result:
                print(tarefa)

        except Exception as erro:
            print(erro)

        finally:
            self.close_connection()



    def filter(self,texto,texto2):
        self.connect()
        try:
            self.cursor.execute(f"""
                SELECT * FROM JOCEYR
                                WHERE NOME LIKE '%{texto}%' OR ESTADO_TAREFA LIKE '%{texto2}%';
                                """)
            result = self.cursor.fetchall()

            for task in result:
                print(task[1],"  -  ",task[4])
                
                
        
        except Exception as erro:
            print(erro)

        finally:
            self.close_connection()



    def delete(self,id):
        self.connect()
        try:
            self.cursor.execute(f'delete from joceyr where id = {id}')
            self.conn.commit()
            self.select()

        except Exception as err:
            print(err)

        finally:
            self.close_connection()



    
    def update(self,dados):
        self.connect()
        try:
            self.cursor.execute(f"""
                UPDATE JOCEYR SET
                    nome = '{dados[1]}',
                    descricao = '{dados[2]}',
                    data_tarefa = '{dados[3]}',
                    estado_tarefa = '{dados[4]}'
                    WHERE id = '{dados[0]}'


                                """)
            self.conn.commit()
            self.select()

        except Exception as erro:
            print(erro)
        
        finally:
            self.close_connection()




    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Conexão encerrada com sucesso!")



if __name__ == "__main__":
    # id = int(input("Digite o id da tarefa a ser alterada: "))
    # nome = input("Digite o novo nome: ")
    # desc = input("Digite a nova descrição: ")
    # data = input("Digite a nova data: ")
    # estado = input("Digite o novo estado: ")
   

    # dados = (id,nome,desc,data,estado)

    db = Database()
    db.connect()
    db.filter('valo', 'er')
    # db.update(dados)
    # db.select()
    # db.insert(task)
    db.close_connection()