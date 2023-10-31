from typing import Any
import mysql.connector

class Database():
    def __init__(self, banco="meuapp") -> None:
        self.banco = banco

    def connect(self):
        self.conn = mysql.connector.connect(host='192.168.22.9',database=self.banco, user="fabrica", password="fabrica@2022")
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("Conectado ao Servidor com  sucesso!", db_info)
        else:
            print("Erro ao conectar!!!")


    def insert(self,clientes):
        self.connect()

        try:
            self.cursor.execute("INSERT INTO clientes (nome, cpf, email, telefone, endereco) VALUES (%s,%s,%s,%s,%s)", (clientes[0],clientes[1],clientes[2],clientes[3],clientes[4]))
            self.conn.commit()
            return "Cadastrada com sucesso!"
        
        except Exception as erro:
            return erro

        finally:
            self.close_connection()
 

    def select(self):
        self.connect()
        try:
            self.cursor.execute("SELECT * FROM clientes")
            result = self.cursor.fetchall()
            return result

        except Exception as erro:
            return erro

        finally:
            self.close_connection()



    def filter(self,texto,texto2):
        self.connect()
        try:
            self.cursor.execute(f"""
                SELECT * FROM clientes
                                WHERE NOME LIKE '%{texto}%' OR CPF LIKE '%{texto2}%';
                                """)
            result = self.cursor.fetchall()

            for task in result:
                print(task[1],"  -  ",task[2])
                
                
        
        except Exception as erro:
            return erro

        finally:
            self.close_connection()



    def delete(self,id):
        self.connect()
        try:
            self.cursor.execute(f'delete from clientes where id = {id}')
            self.conn.commit()
            self.select()

        except Exception as erro:
            print(erro)

        finally:
            self.close_connection()



    
    def update(self,dados):
        self.connect()
        try:
            self.cursor.execute(f"""
                UPDATE clientes SET
                    nome = '{dados[1]}',
                    cpf = '{dados[2]}',
                    email = '{dados[3]}',
                    telefone = '{dados[4]}',
                    endereco = '{dados[5]}'
                    WHERE id = '{dados[0]}'


                                """)
            self.conn.commit()
            self.select()

        except Exception as erro:
            return erro
        
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
    # db.filter('valo', 'er')
    # db.update(dados)
    # db.insert()
    # db.insert(task)
    db.close_connection()